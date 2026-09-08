/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Ui
import "../components"

// Design-time layout only: no settings are persisted or read from the
// backend yet.
Item {
    id: root
    width: 1920
    height: 1080

    ScrollView {
        anchors.fill: parent
        contentWidth: availableWidth
        clip: true

        ColumnLayout {
            width: parent.width
            spacing: Constants.spacingL

            PageHeader {
                title: "Settings"
                subtitle: "App preferences and data-source configuration."
                Layout.fillWidth: true
                Layout.margins: Constants.spacingL
            }

            SectionPanel {
                Layout.fillWidth: true
                Layout.leftMargin: Constants.spacingL
                Layout.rightMargin: Constants.spacingL
                title: "Pricing API Keys"

                ColumnLayout {
                    Layout.fillWidth: true
                    spacing: Constants.spacingS

                    Text {
                        text: "Read from a local .env file (CSFLOAT_API_KEY, BUFF_API_KEY, STEAM_API_KEY). Not editable here yet."
                        font: Constants.smallFont
                        color: Constants.mutedTextColor
                        wrapMode: Text.WordWrap
                        Layout.fillWidth: true
                    }

                    TextField {
                        Layout.fillWidth: true
                        placeholderText: "CSFloat API key"
                        enabled: false
                    }

                    TextField {
                        Layout.fillWidth: true
                        placeholderText: "Steam API key"
                        enabled: false
                    }
                }
            }

            SectionPanel {
                Layout.fillWidth: true
                Layout.leftMargin: Constants.spacingL
                Layout.rightMargin: Constants.spacingL
                Layout.bottomMargin: Constants.spacingL
                title: "About"

                Text {
                    text: "CS2 Loadout Generator — a work-in-progress A-Level Computer Science project."
                    font: Constants.smallFont
                    color: Constants.mutedTextColor
                    wrapMode: Text.WordWrap
                    Layout.fillWidth: true
                }
            }
        }
    }
}
