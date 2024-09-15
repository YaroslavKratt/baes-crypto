
plugins {
    java
    idea
    jacoco
    application
    id("com.diffplug.spotless")
    id("io.freefair.lombok")
}

dependencies {
    implementation("com.opencsv:opencsv:5.9")
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

application {
    mainClass = "kpi.pti.App"
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}

configure<com.diffplug.gradle.spotless.SpotlessExtension> {
    java {
        googleJavaFormat()
        removeUnusedImports()
    }
}