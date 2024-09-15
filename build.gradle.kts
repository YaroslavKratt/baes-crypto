
plugins {
    java
    idea
    jacoco
    application
    id("com.diffplug.spotless")
    id("io.freefair.lombok")
}


dependencies {

}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

application {
    mainClass = "org.example.App"
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}