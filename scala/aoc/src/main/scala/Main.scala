import io.circe.generic.auto.{asJson, HttpBinResponse}
import sttp.client3.{quickRequest, UriContext, basicRequest}

@main def hello: Unit =
  println("Hello world!")
  println(msg)


def msg = sttp.client3.basicRequest.get(uri"https://www.google.com").response(asJson[HttpBinResponse].getRight)