import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    app.setApplicationName("CS2 Loadout Generator")
    app.setOrganizationName("compsci-loadout-project")

    project_dir = Path(__file__).parent
    ui_dir = project_dir / "Ui"


    engine = QQmlApplicationEngine()

    # Allow App.qml to resolve: import Ui
    engine.addImportPath(str(ui_dir.resolve()))

    # Load the Design Studio application entry point
    qml_file = ui_dir / "UiContent" / "App.qml"

    engine.load(QUrl.fromLocalFile(str(qml_file.resolve())))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
