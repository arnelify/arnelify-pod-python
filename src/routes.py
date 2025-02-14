from arnelify_router import ArnelifyRouter

from core.broker.index import broker

from app.middleware.test import testMiddleware

from app.services.first import FirstService
from app.services.second import SecondService

def routes(router: ArnelifyRouter) -> None:

  def SecondAction(ctx: dict) -> dict:
    return SecondService.welcome(ctx)
  broker.subscribe("second.welcome", SecondAction)
  
  def FirstAction(ctx: dict) -> dict:
    newCtx = testMiddleware(ctx)
    return FirstService.welcome(newCtx)
  broker.subscribe("first.welcome", FirstAction)

  def HomeController(ctx: dict) -> dict | str:
    return broker.call("first.welcome", ctx["params"])
  
  router.get("/", HomeController)