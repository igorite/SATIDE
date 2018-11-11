stylesheet = """

    
    QMdiSubWindow{
        background-color: transparent
             }
             
    QFrame#central_frame{
        background-color: #222;
        }
        
    QFrame#mdi_frame{
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
        color: #FFFFFF;
        background-color: #BBB;
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
        text-align: left;
        background-color : transparent;
    }
    
    
    QPushButton:hover[connect=True]{
        background-color : transparent
    }   
             
    QToolBar{
            border:2px solid #999999;
            border-radius: 10px;
            background-color : #333;
        
        }
    
             
        """