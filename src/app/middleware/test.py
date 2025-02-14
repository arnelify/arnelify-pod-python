from core.logger.index import Logger

def testMiddleware(ctx: dict) -> dict:
  numbers = [3, 3, 3]  
  ctx["params"]["numbers"] = numbers
  Logger.primary("TestMiddleware: Let's start the test, guys.\n")  
  return ctx