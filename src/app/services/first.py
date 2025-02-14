from core.logger.index import Logger
from core.broker.index import broker

class FirstService:
    def welcome(ctx: dict):
        params = ctx["params"]
        numbers: dict = params["numbers"]
        
        joined = " + ".join(map(str, numbers))
        
        Logger.primary(f"First: Hey, Second! Can you tell me what {joined} equals?\n")
        
        secondResponse = broker.call("second.welcome", ctx["params"])
        
        if secondResponse.get("code") != 200:
            return secondResponse
        
        response = secondResponse["success"]["response"]
        Logger.primary("First: Great, Second! Thanks a lot!\n")
        
        return response
