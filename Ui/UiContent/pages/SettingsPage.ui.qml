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

// Appearance controls are live (bound to Constants, which every page reads
// its colors/fonts from). Everything else on this page is still
// design-time only - not persisted or read from the backend.
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
                title: "Appearance"

                ColumnLayout {
                    Layout.fillWidth: true
                    spacing: Constants.spacingM

                    RowLayout {
                        Layout.fillWidth: true

                        Text {
                            text: "Dark theme"
                            font: Constants.font
                            color: Constants.textColor
                            Layout.fillWidth: true
                        }

                        Switch {
                            id: darkModeSwitch
                            checked: Constants.darkMode
                            font: Constants.font
                        }

                        Connections {
                            target: darkModeSwitch
                            function onToggled() {
                                Constants.darkMode = darkModeSwitch.checked
                            }
                        }
                    }

                    RowLayout {
                        Layout.fillWidth: true

                        Text {
                            text: "Text size"
                            font: Constants.font
                            color: Constants.textColor
                            Layout.fillWidth: true
                        }

                        ComboBox {
                            id: textSizeCombo
                            wheelEnabled: true
                            Layout.preferredWidth: 100
                            model: ["Small", "Normal", "Large"]
                            currentIndex: 1
                            font: Constants.font
                        }

                        Connections {
                            target: textSizeCombo
                            function onActivated(index) {
                                Constants.fontScale = index === 0 ? 0.85 : (index === 2 ? 1.2 : 1.0)
                            }
                        }
                    }

                    RowLayout {
                        Layout.fillWidth: true

                        Item { Layout.fillWidth: true }

                        Button {
                            id: resetAppearanceButton
                            text: "Reset to defaults"
                            font: Constants.font
                        }

                        Connections {
                            target: resetAppearanceButton
                            function onClicked() {
                                Constants.darkMode = true
                                Constants.fontScale = 1.0
                                textSizeCombo.currentIndex = 1
                            }
                        }
                    }
                }
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
                        text: "Enter API keys for pricing services."
                        font: Constants.smallFont
                        color: Constants.mutedTextColor
                        wrapMode: Text.WordWrap
                        Layout.fillWidth: true
                    }

                    TextField {
                        font: Constants.font
                        Layout.fillWidth: true
                        placeholderText: "CSFloat API key"
                        echoMode: TextInput.Password
                    }

                    TextField {
                        font: Constants.font
                        Layout.fillWidth: true
                        placeholderText: "Steam API key"
                        echoMode: TextInput.Password
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
                    text: "CS2 Loadout Generator — Find your dream loadout given budget and preferences in one click."
                    font: Constants.smallFont
                    color: Constants.mutedTextColor
                    wrapMode: Text.WordWrap
                    Layout.fillWidth: true
                }
            }
        }
    }
}
