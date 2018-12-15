stylesheet = """    
    QMdiSubWindow{
        background-color: transparent
             }
             
    QFrame#central_frame{
        background-color: #222;
        }
        
    QLabel{
        color:#FFF;
        text-align:right;
        font: 14px;
    }
    
    PopUpWindow{
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
         stop:1 rgba(36,63,86,255), stop:0 rgba(65,95,118, 255));
        border: 20px solid black;
    }
    
    QLabel#pop_up_title {
        font: bold 16px;
    }
    
    QFrame#pop_up_title_bar{
         background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
         stop:1 rgba(10, 10, 10, 250), stop:0 rgba(25, 25, 25, 250));
        font: bold 16px;
        border: 1px solid #111;
    }
    
    QFrame#pop_up_main_frame{
        border: 1px solid #111;
    }
    
    QPushButton#close{
        background-color: transparent;
        border: 0px solid black
    }
    
    
    QLineEdit{
        background-color: #444;
        color: #FFF;
        font: 14px;
    }
    
    QLineEdit:hover{
        border:2px solid #337190;
        border-radius:4px;
    }
    
    BaseFunction{
        color: #FFF;
        background-color: #822;
        border-radius: 20px;
    }
    
    BlockCreatorView{
        background-color: #102020;
        
    }
    
    BlockCreatorFunctions{
        border: 2px solid white
    }
    
    CentralCodeFrame{
        border: 2px solid white;
        background-color: #222222;
        border-radius: 50px
    }
    
    QLabel#row_number{
        color:#CCC;
        font: bold 60px;
        text-align:right
    }
    
    BaseVariable{
        background-color: #202080;
        border: 1px solid white;
        border-radius: 5px;
    }
        
    QFrame#mdi_frame{
        background-color: #444;
        border: 2px solid #999999;
        border-radius: 10px;
        }
        
     QFrame#block_creator{
        background-color: #444;
        border: 2px solid #999999;
        border-radius: 10px;
        }
        
    QMdiArea{
        border : 2px solid #999999;
        border-radius: 2px;
        
    }
    QFrame#bar{
        border:2px solid black;
        font-size:20px
    }
    
    QFrame#block_title{
        background-color: transparent;
    }
     QFrame#block_body{
        
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
         stop:1 rgba(0, 0, 0, 250), stop:0 rgba(30, 30, 30, 250));
        border-radius: 20px;
        padding-bottom:60px
    }
    
    QFrame:hover#block_body{
        
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 
        stop:1 rgba(0, 0, 0, 250), stop:0 rgba(150, 150, 30, 250));
        border-radius: 20px;
    }
    
             
    QPushButton{
        color: #ffffff;
        background-color: #333;
        border:1px solid #666;
        border-radius: 2px;
        font-size: 16px;
        padding: 3px;
             }
             
    QPushButton:hover{
        color: #ffffff;
        background-color: #444;
        border:2px solid #337190;
        border-radius: 4px;
        font-size: 16px
             }         
    
    QPushButton[img=True]{
        background-color : transparent;
    }
    
    QPushButton:hover[img=True]{
        background-color : #666;
    }
    QPushButton[connect=True]{
        background-color : transparent
    }
    
     QPushButton[title=True]{
        text-align: left;
        background-color : transparent;
    }
         
    QToolBar{
            border:2px solid #999999;
            border-radius: 10px;
            background-color : #333;
        
        }
    
             
        """