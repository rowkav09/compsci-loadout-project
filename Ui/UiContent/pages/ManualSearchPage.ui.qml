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

Item {
    id: root
    width: 1920
    height: 1080

    property var searchResults: []

    function scheduleSearch() {
        searchTimer.restart()
    }

    function runSearch() {
        var query = searchField.text.trim()
        var weaponName = weaponFilter.currentIndex === 0 ? "" : weaponFilter.currentText
        var rarity = rarityFilter.currentIndex === 0 ? "" : rarityFilter.currentText
        var crate = crateFilter.currentIndex === 0 ? "" : crateFilter.currentText

        if (query.length === 0 && weaponName.length === 0 && rarity.length === 0 && crate.length === 0) {
            root.searchResults = []
            return
        }

        root.searchResults = skinsController.search_text(query, weaponName, rarity, crate)
    }

    Timer {
        id: searchTimer
        interval: 150
        repeat: false
        onTriggered: root.runSearch()
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
                    id: searchField
                    Layout.fillWidth: true
                    placeholderText: "Search by skin or weapon name..."
                    font: Constants.font
                    color: Constants.textColor
                    placeholderTextColor: Constants.mutedTextColor
                    background: Rectangle {
                        color: Constants.surfaceColor
                        border.color: Constants.borderColor
                        radius: Constants.radius
                    }
                    onTextChanged: root.scheduleSearch()
                }

                ComboBox {
                    id: weaponFilter
                    Layout.preferredWidth: 140
                    model: ["Any Weapon", "AK-47", "M4A4", "AWP", "Desert Eagle", "Glock-18"]
                    font: Constants.font
                    background: Rectangle {
                        color: Constants.surfaceColor
                        border.color: Constants.borderColor
                        radius: Constants.radius
                    }
                    onCurrentTextChanged: root.scheduleSearch()
                }

                ComboBox {
                    id: rarityFilter
                    Layout.preferredWidth: 140
                    model: ["Any Rarity", "Consumer", "Industrial", "Mil-Spec", "Restricted", "Classified", "Covert"]
                    font: Constants.font
                    background: Rectangle {
                        color: Constants.surfaceColor
                        border.color: Constants.borderColor
                        radius: Constants.radius
                    }
                    onCurrentTextChanged: root.scheduleSearch()
                }

                ComboBox {
                    id: crateFilter
                    Layout.preferredWidth: 140
                    model: ["Any Crate"]
                    font: Constants.font
                    background: Rectangle {
                        color: Constants.surfaceColor
                        border.color: Constants.borderColor
                        radius: Constants.radius
                    }
                    onCurrentTextChanged: root.scheduleSearch()
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
                    model: root.searchResults

                    delegate: SkinCard {
                        weaponName: modelData.weapon_name || "Unknown weapon"
                        skinName: modelData.name || "Unknown skin"
                        rarity: modelData.rarity || "Unknown"
                        imageSource: modelData.image || ""
                    }
                }
            }
        }
    }
}
