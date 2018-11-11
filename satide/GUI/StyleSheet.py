stylesheet = """

    
    QMdiSubWindow{
        background-color: transparent
             } 
    QFrame#block_title{
        background-color: transparent;
    }
     QFrame#block_body{
        
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(0, 0, 0, 250), stop:0 rgba(30, 30, 30, 250));
        border-radius: 20px;
    }
    
    QFrame:hover#block_body{
        
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(0, 0, 0, 250), stop:0 rgba(150, 150, 30, 250));
        border-radius: 20px;
    }
    
             
    QPushButton{
        color: #FFFFFF;
        background-color: #000;
        border:2 px;
        font-size: 16px
             }
    QPushButton[img=True]{
        background-color : transparent;
    }
    QPushButton[connect=True]{
        background-color : transparent
    }
    
     QPushButton[title=True]{
        background-color : transparent;
    }
    
    
    QPushButton:hover[connect=True]{
        background-color : transparent
    }
    
             
    QPushButton:hover{
        background-color: #111111;
             }
             
             
    QToolBar{
            background : #222222
        
        }
    QToolBar::handle{
        image: url(img/drag.png)
        }    
             
        """