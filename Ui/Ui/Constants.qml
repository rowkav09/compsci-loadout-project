pragma Singleton
import QtQuick

QtObject {
    readonly property FontLoader helveticaBold: FontLoader {
        source: "../fonts/helvetica-bold-3-2_ufonts.com.ttf"
    }

    readonly property int width: 1920
    readonly property int height: 1080

    property string relativeFontDirectory: "fonts"

    // Live appearance state, changed from the Settings page. Everything
    // below that depends on these re-evaluates automatically wherever
    // it's bound.
    property bool darkMode: true
    property real fontScale: 1.0

    readonly property font font: Qt.font({
        family: helveticaBold.name,
        pixelSize: Qt.application.font.pixelSize * fontScale,
        bold: true
    })

    readonly property font largeFont: Qt.font({
        family: helveticaBold.name,
        pixelSize: Qt.application.font.pixelSize * 1.6 * fontScale,
        bold: true
    })

    readonly property font smallFont: Qt.font({
        family: helveticaBold.name,
        pixelSize: Qt.application.font.pixelSize * 0.875 * fontScale,
        bold: true
    })

    readonly property color backgroundColor: darkMode ? "#1C1C1C" : "#EAEAEA"
    readonly property color surfaceColor: darkMode ? "#2A2A2A" : "#DADADA"
    readonly property color borderColor: darkMode ? "#444444" : "#B0B0B0"
    readonly property color textColor: darkMode ? "#EAEAEA" : "#202020"
    readonly property color mutedTextColor: darkMode ? "#9A9A9A" : "#606060"

    readonly property int spacingS: 6
    readonly property int spacingM: 12
    readonly property int spacingL: 20

    readonly property int navRailWidth: 160
}
