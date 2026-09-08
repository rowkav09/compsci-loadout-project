import QtQuick
import QtQuick.Layouts
import Ui
import "components"
import "pages"

Window {
    id: window

    width: 1280
    height: 800
    visible: true
    title: "CS2 Loadout Generator"
    color: Constants.backgroundColor

    readonly property var destinations: ["Loadout Generator", "Manual Search", "Settings"]

    RowLayout {
        anchors.fill: parent
        spacing: 0

        NavRail {
            Layout.fillHeight: true
            Layout.preferredWidth: Constants.navRailWidth
            destinations: window.destinations
            currentIndex: pageStack.currentIndex
            onDestinationSelected: (index) => pageStack.currentIndex = index
        }

        StackLayout {
            id: pageStack
            objectName: "pageStack"
            Layout.fillWidth: true
            Layout.fillHeight: true
            currentIndex: 0

            LoadoutGeneratorPage {}
            ManualSearchPage {}
            SettingsPage {}
        }
    }
}
