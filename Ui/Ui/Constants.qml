pragma Singleton
import QtQuick

QtObject {
    readonly property int width: 1920
    readonly property int height: 1080

    property string relativeFontDirectory: "fonts"

    readonly property font font: Qt.font({
        family: Qt.application.font.family,
        pixelSize: Qt.application.font.pixelSize
    })

    readonly property font largeFont: Qt.font({
        family: Qt.application.font.family,
        pixelSize: Qt.application.font.pixelSize * 1.6
    })

    readonly property font smallFont: Qt.font({
        family: Qt.application.font.family,
        pixelSize: Qt.application.font.pixelSize * 0.85
    })

    readonly property color backgroundColor: "#EAEAEA"
    readonly property color borderColor: "#B0B0B0"
    readonly property color textColor: "#202020"
    readonly property color mutedTextColor: "#606060"

    readonly property int spacingS: 6
    readonly property int spacingM: 12
    readonly property int spacingL: 20

    readonly property int navRailWidth: 160
}
