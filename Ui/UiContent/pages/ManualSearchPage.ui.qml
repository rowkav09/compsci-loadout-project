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

// Design-time layout only: search field, filters and results use static
// sample data and are not wired to SkinsController yet.
Item {
    id: root
    width: 1920
    height: 1080

    ListModel {
        id: sampleResults

        ListElement { weaponName: "AWP"; skinName: "Dragon Lore"; wear: "Field-Tested"; rarity: "Covert" }
        ListElement { weaponName: "Glock-18"; skinName: "Fade"; wear: "Factory New"; rarity: "Restricted" }
        ListElement { weaponName: "USP-S"; skinName: "Kill Confirmed"; wear: "Minimal Wear"; rarity: "Covert" }
        ListElement { weaponName: "M4A1-S"; skinName: "Hyper Beast"; wear: "Field-Tested"; rarity: "Classified" }
        ListElement { weaponName: "P250"; skinName: "Sand Dune"; wear: "Battle-Scarred"; rarity: "Consumer" }
        ListElement { weaponName: "MAC-10"; skinName: "Neon Rider"; wear: "Field-Tested"; rarity: "Classified" }
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: Constants.spacingL

        PageHeader {
            title: "Manual Search"
            subtitle: "Search and filter skins directly from the local dataset."
            Layout.fillWidth: true
            Layout.margins: Constants.spacingL
        }

        SectionPanel {
            Layout.fillWidth: true
            Layout.leftMargin: Constants.spacingL
            Layout.rightMargin: Constants.spacingL

            RowLayout {
                Layout.fillWidth: true
                spacing: Constants.spacingM

                TextField {
                    Layout.fillWidth: true
                    placeholderText: "Search by skin or weapon name..."
                }

                ComboBox {
                    Layout.preferredWidth: 140
                    model: ["Any Weapon", "AK-47", "M4A4", "AWP", "Desert Eagle", "Glock-18"]
                }

                ComboBox {
                    Layout.preferredWidth: 140
                    model: ["Any Rarity", "Consumer", "Industrial", "Mil-Spec", "Restricted", "Classified", "Covert"]
                }

                ComboBox {
                    Layout.preferredWidth: 140
                    model: ["Any Crate"]
                }
            }
        }

        ScrollView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.leftMargin: Constants.spacingL
            Layout.rightMargin: Constants.spacingL
            Layout.bottomMargin: Constants.spacingL
            contentWidth: availableWidth
            clip: true

            Flow {
                width: parent.width
                spacing: Constants.spacingM

                Repeater {
                    model: sampleResults

                    delegate: SkinCard {
                        weaponName: model.weaponName
                        skinName: model.skinName
                        wear: model.wear
                        rarity: model.rarity
                    }
                }
            }
        }
    }
}
