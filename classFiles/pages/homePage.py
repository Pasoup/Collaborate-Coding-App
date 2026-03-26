from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.RoomClass import Room
from classFiles.RoomBox import RoomBox


# -------------------- Main Window --------------------
class Home(QMainWindow):
    def __init__(self, user, ui):
        super().__init__()

        self.ui = ui
        self.ui.setupUi(self)

        self.data = user.getRooms()
        self.name = user.getName()
        self.filtered_rooms = []


        # Make the vertical layout the main layout of the window
        central = QWidget(self)
        central.setLayout(self.ui.verticalLayout)
        self.setCentralWidget(central)


        self.ui.verticalLayoutWidget.deleteLater()


        # Header
        self.ui.homeUserName.setText(str(self.name))

        # Connect search bar to trigger search on every text change
        self.ui.homeSearchBar.textChanged.connect(self.performSearch)

        # Use the grid created by Designer
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        self.ui.scrollAreaWidget.setLayout(self.grid)

        self.colAmount = None
        self.performSearch()

        

        


    # -------------------- Search --------------------
    def performSearch(self):
        text = self.ui.homeSearchBar.text().lower().strip()

        # Show all if search is empty
        if not text:
            self.filtered_rooms = list(self.data)
        else:
            self.filtered_rooms = [
                v for v in self.data
                if text in v.getRoomName().lower()
                or text in v.getDescription().lower()
                or text in str(v.getRoomID()).lower()
            ]

        self.rebuildGrid(True)

    # -------------------- Grid Helpers --------------------
    def clearGrid(self):
        while self.grid.count():
            item = self.grid.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def rebuildGrid(self, ignore=False):
        # Dynamic column count
        someCardWidth = 300
        
        available_width = self.ui.scrollArea.viewport().width()
        columns = max(2, available_width // someCardWidth)

        if (self.colAmount == None):
            self.colAmount = 3
            
        
        elif (columns == self.colAmount and not ignore):
            return
        

        self.clearGrid()
        self.colAmount = columns
        if not self.filtered_rooms:
            return

        

        row = col = 0
        for room in self.filtered_rooms:
            card = RoomBox(room)
            self.grid.addWidget(card, row, col)

            col += 1
            if col >= self.colAmount:
                col = 0
                row += 1


    # -------------------- Responsive Resize --------------------
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.rebuildGrid()
