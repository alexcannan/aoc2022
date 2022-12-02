val scala3Version = "3.2.1"

lazy val root = project
  .in(file("."))
  .settings(
    name := "aoc",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies += "com.softwaremill.sttp.client3" %% "core" % "3.8.3",
    libraryDependencies += "com.softwaremill.sttp.client3" %% "circe" % "3.8.3",
    libraryDependencies += "io.circe" %% "circe-generic" % "0.14.1",
    libraryDependencies += "org.scalameta" %% "munit" % "0.7.29" % Test,
  )
