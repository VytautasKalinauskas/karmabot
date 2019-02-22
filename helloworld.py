# See readme.md for instructions on running this code.

from typing import Any, Dict

class HelloWorldHandler(object):

    def usage(self) -> str:
        return '''
        This is a boilerplate bot that responds to a user query with
        "beep boop", which is robot for "Hello World".

        This bot can be used as a template for other, more
        sophisticated, bots.
        '''

    def handle_message(self, message: Dict[str, Any], bot_handler: Any) -> None:

        content = message['content']
        if 'duok karmos' in content:
            if bot_handler.storage.contains("karma"):
                points = bot_handler.storage.get("karma")
            else:
                points = 0
            points += 1
            bot_handler.storage.put("karma", points)
            content = 'daviau karmos'
        elif 'kiek' in content:
            if bot_handler.storage.contains("karma"):
                content = bot_handler.storage.get("karma")
            else:
                content = 0
        else:
            content = 'negausi'
        bot_handler.send_reply(message, content)
		
handler_class = HelloWorldHandler
