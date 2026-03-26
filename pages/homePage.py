from include.pyside6Import import *
from include.lib import *
from uiFiles.output import Ui_Form
from classFiles.RoomClass import Room
from classFiles.RoomBox import RoomBox


# -------------------- Main Window --------------------
class Home(QObject):
    def __init__(self, user, ui :Ui_Form, window: QMainWindow):
        super().__init__(window)

        self.ui = ui
        self.window = window

        self.data = user.getRooms()
        self.name = user.getName()
        self.filtered_rooms = []


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

        
        self.ui.homeLogoutBtn.clicked.connect(self.gotoLogout)
        self.ui.homeAddRoomBtn.clicked.connect(self.goToAddRoom)
        self.ui.homeCreateRoomBtn.clicked.connect(self.goToCreateRoom)
    
    def gotoLogout(self):
        self.ui.MainPages.setCurrentIndex(0)

    def goToAddRoom(self):
        self.ui.MainPages.setCurrentIndex(0)
    
    def goToCreateRoom(self):
        self.ui.MainPages.setCurrentIndex(0)


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
