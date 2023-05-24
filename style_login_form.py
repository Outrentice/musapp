main_style_line_edit = ('''
    QLineEdit { 
        border-radius: 6px; 
        color:rgb(0, 0, 0); 
        background-color: rgb(255, 255, 255); 
    } 

    QLineEdit:focus { 
        border:1px outset; 
        border-radius: 6px; 
        border-color: rgb(0, 120, 60); 
        color:rgb(0, 0, 0); 
        background-color: rgb(190, 190, 190); 
    }

''')

main_style_push_button = ('''
    QPushButton {
        border-radius: 6px; 
        color:rgb(0, 0, 0); 
        background-color: rgb(190, 190, 190);
    }
    
    QPushButton:hover {
        background-color: rgb(150, 150, 150);
    }
    
    QPushButton:pressed {
        background-color: rgb(190, 190, 190);
    }
''')

main_style = main_style_line_edit + main_style_push_button

sign_up_button_style = ('''
    * {
        border: None;
        background: None;
        color: rgb(70, 70, 70);
        text-decoration: underline;
    }
    
    *:hover {
        color: rgb(0, 0, 0); 
    }
    
    *:pressed {
        color: rgb(70, 70, 70);
    }
''')

error_line_edit_register_style = ('''
    * {
        border:1px outset;
        border-color: rgb(202, 0, 0);
    }
''')

error_label_register_style = ('''
    * {
        color: rgb(202, 0, 0);
    }
''')

volume_slider_style = ("""
    QSlider::groove:horizontal {
        border-radius:1%;       
        height: 6px;              
        margin: -1px 0;           
    }
    QSlider::handle:horizontal {
        background-color: rgb(85, 17, 255);
        border: 0.5px solid  rgb(85, 17, 255);
        height: 12px;     
        width: 12px;
        margin: -4px 0;     
        border-radius: 7px;
        padding: -4px 0px;  
    }
    QSlider::add-page:horizontal {
        background: darkgray;
    }
    QSlider::sub-page:horizontal {
        background: rgb(0, 120, 60);
    }"

""")

track_time_slider_style = ("""
    QSlider::groove:horizontal {
        border-radius:1%;       
        height: 10px;              
        margin: -1px 0;           
    }
    QSlider::handle:horizontal {
        height: 6px;     
        width: 6px;
    }
    QSlider::add-page:horizontal {
        background: darkgray;
    }
    QSlider::sub-page:horizontal {
        background: rgb(0, 120, 60);
    }"
""")
