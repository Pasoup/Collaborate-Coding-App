from include.pyside6Import import *
from classFiles.RoomClass import Room

# -------------------- Room Card --------------------
class RoomBox(QWidget): 
    def __init__(self, room: Room): 
        super().__init__() 
        self.room = room 
        layout = QVBoxLayout(self) 
        layout.setContentsMargins(6, 6, 6, 6) 
        layout.setSpacing(4) 

        title = QLabel(f"{self.room.getRoomID()} : {self.room.getRoomName()}") 
        title.setStyleSheet( f"background-color:{self.room.getColor()};" "font-weight:bold;" "padding:6px;" ) 
        desc = QLabel(self.room.getDescription()) 
        desc.setWordWrap(True) 

        desc.setStyleSheet( "background-color:#4C4C4C;" "color:white;" "padding:6px;" ) 
        self.setStyleSheet( "background-color:#2E2E2E;" # Card background 
                           "border:2px solid #888;" # Border color 
                           "border-radius:12px;" # Rounded corners 
                           ) 
        layout.addWidget(title, stretch=3) 
        layout.addWidget(desc, stretch=7)

        self.setMinimumSize(220, 140) 
        self.setMaximumSize(440, 280) 
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Handle Hover 
        self.anim = QPropertyAnimation(self, b"geometry") 
        self.anim.setDuration(400) 
        self.anim.setEasingCurve(QEasingCurve.OutCubic) 
        self.baseGeometry = None 
        self.setMouseTracking(True) 
        
        
        # ####################################################################################
        # ---------------------- Sound Homework Part 1 ---------------------- # 
        # self.QSE = QSoundEffect() # self.QSE.setSource(QUrl.fromLocalFile("rabbit_hit.wav")) 
        # ####################################################################################
        # ----------------------------- Animation Homework --------------------------------------- # when enter hover state 
    def enterEvent(self, event):
        if self.baseGeometry is None: 
            self.baseGeometry = self.geometry() 
        rect = self.baseGeometry 
        scale = 1.1 
        newWidth = int(rect.width() * scale) 
        newHeight = int(rect.height() * scale) 
        dx = (newWidth - rect.width()) // 2 
        dy = (newHeight - rect.height()) // 2 
        scaledRect = QRect( rect.x() - dx, rect.y() - dy, newWidth, newHeight ) 
        self.anim.stop() 
        self.anim.setStartValue(self.geometry()) 
        self.anim.setEndValue(scaledRect) 
        self.anim.start() 
            
    #####################################################################
    # ---------------------- Sound Homework Part 2 ----------------------
    # self.QSE.play() event.accept() # Leave hover state 
    
    def leaveEvent(self, event): 
        if self.baseGeometry: 
            self.anim.stop() 
            self.anim.setStartValue(self.geometry()) 
            self.anim.setEndValue(self.baseGeometry) 
            self.anim.start() 
            event.accept() 
        
    def mousePressEvent(self, event): 
        dialog = QDialog(self) 
        dialog.setWindowTitle("Room Page") 
        layout = QVBoxLayout(dialog) 
        layout.addWidget(QLabel(f"Room Page: {self.room.getRoomID()} - {self.room.getRoomName()}")) 
        dialog.exec()