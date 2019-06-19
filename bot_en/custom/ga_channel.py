import asyncio
import inspect
from sanic.response import json
import logging
import uuid
from asyncio import Queue, CancelledError
from sanic import Sanic, Blueprint, response
from sanic.request import Request
from typing import Text, List, Dict, Any, Optional, Callable, Iterable, Awaitable
from rasa.core.channels.channel import UserMessage, OutputChannel
from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import CollectingOutputChannel, QueueOutputChannel

import rasa.utils.endpoints
from rasa.constants import DOCS_BASE_URL
from rasa.core import utils


try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

logger = logging.getLogger(__name__)



class GoogleConnector(InputChannel):
    """A custom http input channel.

    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""

    @classmethod
    def name(cls):
        return "google_home"

    @staticmethod
    async def on_message_wrapper(on_new_message, text, queue, sender_id):
        collector = QueueOutputChannel(queue)

        message = UserMessage(
            text, collector, sender_id, input_channel=GoogleConnector.name()
        )
        await on_new_message(message)

        await queue.put("DONE")

    async def _extract_sender(self, req):
        return req.json.get("user", None)

    # noinspection PyMethodMayBeStatic
    def _extract_message(self, req):
        return req.json.get("inputs", None)

    def stream_response(self, on_new_message, text, sender_id):
        async def stream(resp):
            q = Queue()
            task = asyncio.ensure_future(
                self.on_message_wrapper(on_new_message, text, q, sender_id)
            )
            while True:
                result = await q.get()
                if result == "DONE":
                    break
                else:
                    await resp.write(response.json(result) + "\n")
            await task

        return stream

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            inspect.getmodule(self).__name__,
        )

        # noinspection PyUnusedLocal
        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request):
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request: Request):
            sender_id = await self._extract_sender(request)
            sender_id = sender_id['userId']
            intent = self._extract_message(request)[0]['intent']
            text = self._extract_message(request)[0]['rawInputs'][0]['query']
            should_use_stream = rasa.utils.endpoints.bool_arg(
                request, "stream", default=False
            )

            if should_use_stream:
                return response.stream(
                    self.stream_response(on_new_message, text, sender_id),
                    content_type="text/event-stream",
                )
            else:
                if intent == 'actions.intent.MAIN':
                    message = "<speak>Welcome back <break time=\"1\"/> This is the Oticon-powered Google Assistant skill. You can talk to the OPN chatbot.</speak>"			 
#                    message = "Hello!"
                else:
                    collector = CollectingOutputChannel()
                    # noinspection PyBroadException
                    try:
                        await on_new_message(
                            UserMessage(
                                text, collector, sender_id, input_channel=self.name()
                            )
                        )
                        responses = [m["text"] for m in collector.messages]
                        message = responses[0]

                

                    except CancelledError:
                        logger.error(
                            "Message handling timed out for "
                            "user message '{}'.".format(text)
                        )
                        message = "sorry..."
                    except Exception:
                        logger.exception(
                            "An exception occured while handling "
                            "user message '{}'.".format(text)
                        )
                        message = "sorry..."
                
                r = response.json(
                {
                  "conversationToken": "{\"state\":null,\"data\":{}}",
                  "expectUserResponse": 'true',
                  "expectedInputs": [
                    {
                      "inputPrompt": {
                       "initialPrompts": [
                        {
                          "ssml": message
                        }
                      ]
                     },
                    "possibleIntents": [
                    {
                      "intent": "actions.intent.TEXT"
                    }
                   ]
                  }
                 ]
                })
                return r

        return custom_webhook
