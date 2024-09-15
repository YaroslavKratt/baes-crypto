pluginManagement {
    plugins {
        java
        application
        id("com.diffplug.spotless") version "6.25.0"
        id("io.freefair.lombok") version "8.7.1"
    }
    repositories {
        mavenCentral()
        gradlePluginPortal()
    }
}





dependencyResolutionManagement {
    repositories {
        mavenCentral()
    }
}

rootProject.name = "baes-crypto"