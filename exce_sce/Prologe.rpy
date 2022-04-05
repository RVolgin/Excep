init:
    $ mods["Exception"] = "Исключение"
    
    #bg
    image bg 33_oldbus_day= "exception/bg/33_oldbus_day.jpg"
    image bg 33_oldbus_int = "exception/bg/33_oldbus_int.jpg"
    image bg 33_oldbus_night = "exception/bg/33_oldbus_night.jpg"
    image bg aka1 = "exception/bg/aka1.png"
    image bg aka2 = "exception/bg/aka2.png"
    image bg ddr_ext_camp_entrance_day = "exception/bg/ddr_ext_camp_entrance_day.jpg"
    image bg ddr_ext_camp_entrance_night = "exception/bg/ddr_ext_camp_entrance_night.jpg"
    image bg ddr_ext_camp_entrance_sunset = "exception/bg/ddr_ext_camp_entrance_sunset.jpg"
    image bg ddr_ext_houses_day = "exception/bg/ddr_ext_houses_day.jpg"
    image bg ddr_ext_houses_night = "exception/bg/ddr_ext_houses_night.jpg"
    image bg ddr_ext_houses_sunset = "exception/bg/ddr_ext_houses_sunset.jpg"
    image bg ddr_ext_square_day = "exception/bg/ddr_ext_square_day.jpg"
    image bg ddr_ext_square_night = "exception/bg/ddr_ext_square_night.jpg"
    image bg ddr_ext_square_sunset = "exception/bg/ddr_ext_square_sunset.jpg"
    image bg int_nomus_club_day = "exception/bg/int_nomus_club_day.jpg"
    image bg moon = "exception/bg/moon.png"
    image bg moon_01 = "exception/bg/moon_01.png"
    image bg oldday1 = "exception/bg/oldday1.jpg"
    image bg oldday2 = "exception/bg/oldday2.jpg"
    image bg oldlag1_night = "exception/bg/oldlag1_night.jpg"
    image bg oldlag3 = "exception/bg/oldlag3.jpg"
    image bg oldnight = "exception/bg/oldnight.jpg"
    image bg oldnight1 = "exception/bg/oldnight1.jpg"
    image bg re_tel = "exception/bg/re_tel.png"
    image bg ryuuketu1 = "exception/bg/ryuuketu1.png"
    image bg ryuuketu2 = "exception/bg/ryuuketu2.png"
    image bg sora_01 = "exception/bg/sora_01.png"
    image bg sora_inverse = "exception/bg/sora_inverse.png"
    image bg sora2 = "exception/bg/sora2.png"
    image bg Unter_den_Linden = "exception/bg/Unter_den_Linden.jpg"
    image bg ddr_ext_storage_day = "exception/bg/ddr_ext_storage_day.jpg"


    #cg
    image cg 321-vosstanovleno = im.Scale("exception/cg/321-vosstanovleno.png",1920,1080)
    image cg fire_books = im.Scale("exception/cg/fire_books.jpg",1920,1080)
    image cg illustration = im.Scale("exception/cg/illustration.png",1920,1080)
    image cg lena = im.Scale("exception/cg/Lena.png",1920,1080)
    image cg mg42 = im.Scale("exception/cg/mg42.jpg",1920,1080)
    image cg war = im.Scale("exception/cg/war.png",1920,1080)

    #sprite
    #Александра
    image al base = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_base_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_base_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_base_normal.png"))

    image al indifference = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_indifference_normal.png", ), im.matrix.tint(0.94, 0.82, 1.0) ), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal//al_indifference_normal.png", ), im.matrix.tint(0.63, 0.78, 0.82) ), 
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_indifference_normal.png", ) )
    
    image al sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_sad_normal.png", ), im.matrix.tint(0.94, 0.82, 1.0) ), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_sad_normal.png", ), im.matrix.tint(0.63, 0.78, 0.82) ), 
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_sad_normal.png", ) )

    image al shy = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_shy_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_shy_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_shy_normal.png"))
    
    image al smileh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_smile_h_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_smile_h_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_smile_h_normal.png"))
    
    image al smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_smile_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_smile_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_smile_normal.png"))
    
    image al surprise = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_surprise_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_surprise_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_surprise_normal.png"))
    
    image al tongueh = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_tongueh_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_tongueh_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_tongueh_normal.png"))
    
    image al tongue = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_tongueh_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_tongueh_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/normal/al_tongueh_normal.png"))

    image al base close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_base_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_base_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_base_close.png"))

    image al indifference close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_indifference_close.png", ), im.matrix.tint(0.94, 0.82, 1.0) ), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close//al_indifference_close.png", ), im.matrix.tint(0.63, 0.78, 0.82) ), 
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_indifference_close.png", ) )
    
    image al sad close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_sad_close.png", ), im.matrix.tint(0.94, 0.82, 1.0) ), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_sad_close.png", ), im.matrix.tint(0.63, 0.78, 0.82) ), 
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_sad_close.png", ) )

    image al shy close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_shy_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_shy_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_shy_close.png"))
    
    image al smileh close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_smile_h_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_smile_h_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_smile_h_close.png"))
    
    image al smile close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_smile_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_smile_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_smile_close.png"))
    
    image al surprise close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_surprise_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_surprise_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_surprise_close.png"))
    
    image al tongueh close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_tongueh_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_tongueh_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_tongueh_close.png"))
    
    image al tongue close = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_tongueh_close.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_tongueh_close.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/close/al_tongueh_close.png"))

    image al base far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_base_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_base_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_base_far.png"))

    image al indifference far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_indifference_far.png", ), im.matrix.tint(0.94, 0.82, 1.0) ), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far//al_indifference_far.png", ), im.matrix.tint(0.63, 0.78, 0.82) ), 
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_indifference_far.png", ) )
    
    image al sad far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_sad_far.png", ), im.matrix.tint(0.94, 0.82, 1.0) ), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_sad_far.png", ), im.matrix.tint(0.63, 0.78, 0.82) ), 
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_sad_far.png", ) )

    image al shy far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_shy_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_shy_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_shy_far.png"))
    
    image al smileh far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_smile_h_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_smile_h_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_smile_h_far.png"))
    
    image al smile far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_smile_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_smile_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_smile_far.png"))
    
    image al surprise far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_surprise_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_surprise_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_surprise_far.png"))
    
    image al tongueh far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_tongueh_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_tongueh_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_tongueh_far.png"))
    
    image al tongue far = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_tongueh_far.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_tongueh_far.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "exception/sprites/al/far/al_tongueh_far.png"))



#Брандт
    image br normal  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_normal.png") )
    
    image br angry  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_angry.png") )
    
    image br laugh  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_laugh.png") )
    
    image br rage  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_rage.png") )

    image br scared  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_scared.png") )
    
    image br smile  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/br/br_body.png",(0,0), "exception/sprites/br/br_n.png",(0,0), "exception/sprites/br/br_smile.png") )

#Грета

    image gr normal  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_normal.png") )

    image gr smile  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_smile.png") )

    image gr serious  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_1_form.png",(0,0), "exception/sprites/gr/gr_1_serious.png") )

    image gr smile2  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_smile2.png") )

    image gr shy  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_shy.png") )

    image gr happy  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_happy.png") )

    image gr laugh  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_2_form.png",(0,0), "exception/sprites/gr/gr_2_laugh.png") )

    image gr angry  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_angry.png") )

    image gr sad  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_sad.png") )

    image gr surprise  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_3_form.png",(0,0), "exception/sprites/gr/gr_3_surprise.png") )

    image gr tender  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_4_form.png",(0,0), "exception/sprites/gr/gr_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_4_form.png",(0,0), "exception/sprites/gr/gr_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_4_form.png",(0,0), "exception/sprites/gr/gr_4_tender.png") )
    
    image gr scared  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_4_form.png",(0,0), "exception/sprites/gr/gr_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_4_form.png",(0,0), "exception/sprites/gr/gr_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/gr/gr_4_form.png",(0,0), "exception/sprites/gr/gr_4_scared.png") )

#Фритхельм
    image fr normal  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_normal.png") )

    image fr laugh  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_laugh.png") )

    image fr grin  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_grin.png") )

    image fr dontlike  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_dontlike.png") )

    image fr sad  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_sad.png") )

    image fr shy  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_shy.png") )

    image fr smile  = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "exception/sprites/fr/fr_1_pioneer.png",(0,0), "exception/sprites/fr/fr_1_smile.png") )














    #music
    $ ewige_wiederkunft = "exception/music/ewige_wiederkunft.mp3"
    $ hm06_27 = "exception/music/hm06_27.ogg"
    $ holocaust = "exception/music/holocaust.mp3"
    $ Iwakannnohatuga = "exception/music/iwakannnohatuga.mp3"
    $ jeremy_soule_silent_battlefield = "exception/music/jeremy_soule_silent_battlefield.mp3"
    $ mienai = "exception/music/mienai.ogg"
    $ msys07 = "exception/music/msys07.ogg"
    $ none_dark_desperation = "exception/music/none_dark_desperation.mp3"
    $ unus_mundus = "exception/music/unus_mundus.mp3"
    $ v_tylu_vraga_2_bratya_po_oruzhiyu_lis_pustyni_pered_boem = "exception/music/v_tylu_vraga_2_bratya_po_oruzhiyu_lis_pustyni_pered_boem.mp3"
    $ v_tylu_vraga2_bratya_po_oruzhiyu_lis_pustyni_boj_v = "exception/music/v_tylu_vraga2_bratya_po_oruzhiyu_lis_pustyni_boj_v.mp3"
    $ waking_up = "exception/music/waking_up.mp3"


    #sound
    $ sfx_kar98ks = "exception/sound/kar98ks.wav"
    $ sfx_MG_42 = "exception/sound/MG_42.mp3"
    $ sfx_mg42 = "exception/sound/mg42.mp3"
    $ sfx_mosin = "exception/sound/mosin.wav"
    $ sfx_p38 = "exception/sound/p38.wav"
    $ sfx_pps41 = "exception/sound/ppsh41.mp3"
    $ sfx_svt40 = "exception/sound/svt40.wav"
    $ sfx_valter = "exception/sound/valter.mp3"
    $ ambience_rain = "exception/sound/rain.mp3"

init 2:
    #characters
    $ colors['br'] = {'night': (226, 199, 112), 'sunset': (226, 199, 112), 'day': (226, 199, 112), 'prolog': (226, 199, 112)}
    $ names['br'] = "Брандт"
    $ store.names_list.append('br')
    
    $ colors['gr_ddr'] = {'night': (255, 242, 0), 'sunset': (255, 242, 0), 'day': (255, 242, 0), 'prolog': (255, 242, 0)}
    $ names['gr_ddr'] = "Грета"
    $ store.names_list.append('gr_ddr')
    #$ br = Character (u'Брандт', color="#E2C779", what_color="E2C779")
    $ fa = Character (u'Отец', color="#E2C779", what_color="E2C779")
    $ mo = Character (u'Мама', color="#E2C779", what_color="E2C779")
    #$ gr_ddr = Character (u'Грета', color="#FFF200", what_color="E2C779")
    $ pi_ddr = Character (u'Ребёнок', color="#E2C779", what_color="E2C779")
    $ di_ddr = Character (u'Директор', color="#E2C779", what_color="E2C779")
    $ br_un = Character (u'{color=#E2C779}Брандт{/color}|{color=#B956FF}Лена{/color}', what_color="E2C778")
    
  
  

label Exception:
    scene black
    menu:
        "Пролог":
            jump exc_prolog
        "День 1":
            jump exc_day1
            
label exc_prolog:
    screen udl1():
        text "16:30 по БВ. 29 мая 1954 год. Берлин. ГДР. \n\n -Остановка Унтер-ден-Линден!" xalign 0.5 yalign 0.5 size 60
        
    show screen udl1 with dissolve
    $ renpy.pause(2.5, hard=True)
    hide screen udl1 with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 3
    window show
    "Лишь голос кондуктора вернул меня к реальности. Я успел выскочить в последнюю секунду до того, как трамвай тронется дальше." 
    scene bg Unter_den_Linden with dissolve
    "Летняя погода всё больше вступала в свои права, покрывая всё вокруг теплом."
    "Это не могло не отразиться на парке, по которому я прохожу почти каждый день, ибо он является частью моего типичного пути до дома, одной из самых прекрасных его частей."
    "Унтер-ден-Линден - самый лучший бульвар в Германии. Своим великолепием он обязан липам, что уже расцвели и окружают его со всех сторон своим великолепием."
    "Сам же бульвар, будто водный поток, он то и дело переливается, меняя архитектуру, настроение, цвет, направление движения."
    "Прямо одна из главных артерий Берлина... Он же ведет к Бранденбургским Воротам и соединяет нас с... Германией. Только другой. Да. Германии нынче две."
    "Жаль, что идти мне по нему не особо долго, скоро сворачивать. Обычно я иду здесь неторопливо, наслаждаясь красотами, но сегодня я шагаю необычайно быстро для себя."
    "Ибо больше всего на свете сейчас хочу попасть в свою комнату. Этому способствует всеобщая усталость, особенно в плане мыслительной деятельности."
    scene anim prolog_1 with dissolve
    "Вот и дом... Да, в комнату, в кровать..."
    fa "Брандт."
    stop music fadeout 2
    play music music_list["just_think"] fadein 3
    "Послышался твёрдый голос. Он тут же меня остановил. А ведь оставалось совсем чуть-чуть... Тяжело вздохнув, я произнёс:"
    br "-Да, отец?"
    fa "-Садись, есть разговор."
    "Зайдя в зал, я послушно сел в кресло. Голова трещала и болела после экзаменов, причём по самым худшим предметам, которые только могло придумать человечество."
    "Отец был в своей темной форме со светло-зелеными просветами, будто собирался на парад, ему не хватало только медалей. А у него их было немало. Он герой Второй Мировой Войны."
    fa "Как экзамены?"
    br "Я легко их одолел. Пришлось разве что поскандалить с учителем истории... Упорно не хотела ставить мне высокую оценку."
    fa "Да? И почему же?"
    br "Не знаю, наверно, я ей просто не нравлюсь. В любом случае, я успешно всё сдал. Так что... Очередное лето проведу спокойно."
    fa "Вот об этом речь и пойдёт. Ты молодец, что достойно всё сдал, я горжусь тобой. Но этим летом ты кое-куда отправишься. Уверяю тебя, это пойдёт тебе только на пользу. И это не обсуждается."
    "Я напрягся, он говорил это довольно серьёзным тоном, будто был готов, что вот-вот будет спор. Я старался не выдать своего беспокойства."
    br "Куда, отец?"
    fa "В очень хорошее место, тебе там понравится, поверь. Заодно немного поработаешь. Может, познакомишься с кем-нибудь... А то, что ни лето, ты сидишь в своей комнате за книгой. "
    br "Но..."
    "Было начал я, но он перебил."
    fa "Извини. Ты умный мальчик, безусловно, один из лучших учеников школы, но всё равно, постоянно так нельзя, согласись."
    br "Познакомиться? Так я не вижу в этом никакой необходимости. Всё равно мне почти не с кем, и не о чем разговаривать. Книги гораздо интереснее, чем люди. Разве для поддержания нормального функционирования моего организма тренировок недостаточно? Зачем меня ещё и отправлять куда-то для этого. Кстати, так куда?"
    fa "В лагерь."
    "Тут я уже не смог сдержать своих эмоций и удивленно переспросил:"
    br "Куда?!"
    fa "В пионерский лагерь. Будешь вожатым."
    "На своём лице я не показал ни капли той злости и разочарования, что в тот же миг начали переполнять меня."
    br "Понятно. Приказ партии?"
    fa "Не приказ, а просто моя личная инициатива. Тебе там понравится, я уверен."
    "Мне понравится в любой части моей страны. Но не в таком виде."
    br "Я отказываюсь."
    fa "Нет, ты не можешь. Всё уже договорено и, местами, оплачено."
    br "Но мне уже есть 18, и я имею право отказаться! Как хочу, так и провожу лето! Последнее в жизни, между прочим!"
    fa "Вот и запомнишь его как следует. И пока ты не окончил школу, права такого не имеешь, Брант. Решение окончательное."
    "Чёрт бы его побрал! Вот делать мне больше нечего... Это ж неприятности сплошные. Ещё лагерь... Стиснув зубы, стараясь больше не показывать недовольства, я проговорил:"
    stop music fadeout 2
    br "Хорошо, а куда ехать?"
    "Я даже нашёл в себе силы улыбнуться, несмотря на то, что, по сути, все мои планы на спокойное лето были уничтожены одним, ни капли не зависящим от меня решением."
    fa "Лагерь Штайнкауз. Под Дрезденом. "
    "Вот как. А разве от этого города не остались одни лишь руины?"
    br "Я понял. Пойду, очень устал. "
    fa "Не буду тебя задерживать."
    "Я было повернулся и пошёл..."
    fa "И да, ты едешь не один. Ещё две девочки из, по-моему, твоего класса, едут с тобой. "
    "Ещё чего не хватало... "
    br "И кто? "
    fa "Лена. Такая, с двумя хвостиками. И её подруга. Как же её зовут... "
    br "Грета."
    "Пробубнил я."
    br "Она только с ней и разговаривает. И то не всегда."
    fa "Она это кто? "
    br "Лена. "
    fa "Хмм, ясно. А ты с ней не пробовал общаться? "
    "Заняться мне больше нечем..."
    br "Нет, с какой стати?"
    fa "Ладно, просто поинтересоваться решил."
    play sound sfx_close_door_1
    "На замок, как всегда. Но сегодня особенно. После тяжёлого дня и внезапно свалившегося на меня лагеря, я видеть никого не хочу... "
    "Лежу на кровати и лицезрею потолок. "
    "Вожатым... Ещё и с ними. Мда, это будет явно \"лучшее\" лето в моей жизни. "
    play music unus_mundus fadein 3
    "Вернее, лучшая промывка мозгов в моей жизни. Как будто самой коммунистической пропаганды недостаточно... "
    "Они думают, что мы смирились с этим. Что с этим смирился я. Спросите с чем? С оккупацией! Большевики нас страной-то сделали только несколько лет назад! И то, только для замыливания глаз! На самом деле, это всё та же оккупация! "
    "Из-за них Столица нашей страны и разделена на две части... И я уже сколько лет не вижу свою маму. Надеюсь, ей там, на другой стороне, хорошо. "
    "Да даже чёрт с ней, политикой. О моих слабых навыках общения с девушками и детьми можно слагать легенды. "
    "В моих мыслях почему-то всплыла Лена. Она была очень тихой девочкой с зелёными глазами и двумя хвостиками. Других причёсок она не носила. Фамилия, кажется… Нойманн. "
    "Она отлично говорит по-немецки. Хотя по виду она не совсем похожа на немку... Лена появилась в нашем классе совершенно внезапно и почти ни с кем, кроме Греты, не общалась. Даже когда нам её представляли, она вся залилась краской, как помидор."
    "Училась она хорошо, в этом плане мы были с ней примерно равны (за исключением исторички, само собой). Разве что, она была добрее, чем я. Помогала девчонкам с домашней работой. Ещё ей явно не нравилась физическая культура."
    "Впрочем, чего упрекать человека в этом? Ну не её это, дальше что? Зато она отлично рисует и даже занимает первые места в школьных художественных конкурсах. "
    "Что-то, может быть, и было в ней такое... Загадочное, и, возможно, милое. Но я был всегда занят либо учёбой, либо тренировками. Да и она особо не проявляла инициативу. Хотя..."
    "Если так подумать, я как минимум несколько... Десятков раз ловил на себе её взгляд... И когда я это делал, она тут же краснела и снова продолжала писать, или утыкалась в книгу или учебник. "
    "Ну и что? Подумаешь, смотрела. Кто угодно может смотреть. Это ведь не может говорить о чём-то. Но и не каждая заливается краской при взгляде. "
    stop music fadeout 2
    th "-Грррр..." 
    "Я обволок голову подушкой и постарался уснуть. Устал."
    scene black with dissolve
    window hide

   #======здесь что-то сделать для переключения персонажа 
    screen ud2():
        text "19:00 по БВ. 29 мая 1954 год. Берлин. ГДР." xalign 0.5 yalign 0.5 size 60
    
    show screen ud2 with dissolve
    $ renpy.pause(2.5, hard=True)
    hide screen ud2
    
    scene bg Unter_den_Linden with dissolve
    play music music_list["trapped_in_dreams"] fadein 3
    
    "Всё тело поглотила усталость. Такое чувство, что тебя выжали, как лимон. Даже Унтер-ден-Линден и его липы не смогли поднять мне настроение. Я буквально тащила своё тело до дома. Вот уже сворачивать... "
    "Домой, домой, домой..."
    "Было лишь в моих мыслях. Я даже едва не уронила из рук свои работы, над которыми так долго трудилась. В другой же руке, уже красными пальцами, я держала тяжёлый портфель, который был переполнен книгами. "
    play sound sfx_open_door_1
    scene anim prolog_1 with dissolve
    "Наконец..."
    "Рисунки оказались на полу, будто после оценки их преподавателем они потеряли всякую ценность. Портфель же полетел в самый дальний угол комнаты. Юбка улетела в одну сторону, и, кажется, упала на стол рядом со стопкой учебников и тетрадок."
    "Рубашка улетела другую сторону, упав на холст и угодив рукавом в цветную воду для кисточек. Ещё чуть-чуть, и она может сползти на мольберт..."
    "Но собственно её падение на краски меня уже ни капли не волновало."
    "Для меня важнее другое \"падение\" в самое желанное мною место на свете в данный момент – кровать. После нескольких бессонных ночей это казалось мне лучшим событием в моей биографии. "
    "\"Как сказала бы Лена, глядя на кровать: Если любишь человека - дай ему поспать\". "
    "Никакое вечернее солнце конца мая не помешает мне, наконец-то, уснуть!"
    "Тепло, мягко, хорошо, просто благодать..."
    "Неделя экзаменов была невероятно напряжённой... Что обычная школа, что художка... Столько требований, столько заданий. И всё надо было делать точно, без малейшей запинки и ошибочки ради высокой оценки."
    "Неудивительно, что в Германии всегда была так развита наука и технологии... Да что уж там, куда ни глянь, всё как-то правильно, для людей, что ли. "
    "Не сказала бы, что на моей Родине хуже, но учитывая то, что здесь было, и все эти разрушения... Выглядит и работает так, будто ничего и не было. Не было войны... Не было жертв и разрушений, не было смерти. "
    "Я не ненавижу Германию за то, что они сделали. Сами немцы в большинстве уже осознали, что будущее - за Революцией, а их чудовищная идеология несла лишь ужас. Моя семья хлебнула от этого по полной... Хорошо, хоть целы остались. А теперь вовсе здесь, в уже ГДР..."
    play sound sfx_knocking_door_outside
    un "Да?"
    mo "Ты уже дома? Я-то думала, что ты ещё не пришла... "
    un "Мама! "
    "Мы обнялись. "
    mo "Как ты, девочка моя?"
    "Спросила она ласково, но с нотками строгости."
    mo "Всё сдала? "
    un "Да, мама. Всё хорошо. Проблем никаких нет. Впереди лишь лето..."
    mo "Хи, а рубашку свою ты на радостях решила покрасить? "
    "Мы засмеялись. "
    un "А где папа?"
    mo "Он ещё на учениях..."
    un "Он что, по ночам летает?!"
    "Мой отец, несмотря на окончание войны, всё ещё служит в ГСВГ. Прошёл настоящий ад, защитив нас с мамой и страну. Он лётчик. "
    mo "А как же? Надо уметь быть в боевой готовности в любое время суток... Не переживай, он вернётся домой."
    un "Эх..."
    mo "Но и он на месте не сидит! Он раздобыл тебе кое-что! "
    un "Что же это может быть?"
    "Спросила я, сладко зевнув."
    mo "Этим летом ты поедешь в лагерь под Дрезденом. Будешь вожатой. "
    "Она \"торжественно\" вручила мне две путёвки. Пионер лагерь Штайнкаутз (Совёнок). "
    "Я не знала, как на это реагировать. Я была в пионер-лагере, но одно дело это просто быть пионером, а другое вожатым, да ещё и с немецкой спецификой... Ведь я была пионером Ленина, а они все Тельмановцы."
    un "Это здорово мам, данке. Но я не хочу. "
    mo "То есть как? Почему, доченька? "
    "В её голосе было слышно тревогу. Я опустила глаза вниз. На самом деле, мне мешает во многом моя собственная лень."
    mo "Лен, ты всё время сидишь дома либо за уроками, либо не отходишь от рисования. А так хотя бы отдохнёшь на природе, увидишь хороший город. И... Вдруг найдёшь себе мальчика! "
    un "Мама! "
    "Сказала я и укрылась с головой одеялом. "
    mo "Что? Тебе ведь уже 18, Леночка... Никогда не знаешь, где и как найдёшь свою любовь."
    "Да я уже, честно говоря. И никто мне кроме него не нужен. "
    mo "Кстати... Мне кажется, я слышала, с тобой едет кто-то ещё из твоего класса. Имя такое хорошее, немец."
    "Мама что-то говорила параллельно, но я не слышала её. Теперь, когда я снова подумала он нём, поток моих мыслей было трудно остановить."
    "Он такой... Красивый, умный..."
    mo "Как же его зовут..."
    "Мне он приглянулся сразу, когда мы приехали в Германию по папиной службе, и я поступила в эту школу. "
    mo "А, вспомнила!  "
    "Он сразу для меня выделился среди остальных парней. Они были в большинстве своём глуповатыми и неинтересными. Его зовут..."
    mo "Брант"
    "Брант."
    un "БРАНТ?!"
    "Переспросила я, стараясь не показать целого всплеска чувств, прокатившегося по всему телу. Я ощутила, как моё лицо будто охватил пожар."
    mo "Да, он едет с тобой. А что? "
    "Спросила она кокетливо."
    un "Ничего, мам,"
    "Пробурчала я, из под одеяла. "
    un "Я устала, Гуттен Нахт."
    mo "Гуттен нахт, майн либе. "
    "Сказала мама и, выключив свет, закрыла дверь."
    "Сердце бешено колотилось. Он едет со мной в лагерь?! Боже, не бывает таких совпадений! Как же? Он ведь будет ещё ближе, чем в школе."
    "У нас будет шанс, ну... Поговорить, познакомиться поближе, в конце концов. Он ведь не задира какой-нибудь, никогда никого не обижал, даже наоборот, я видела, как он защищал одного младшеклассника от задир, что, несомненно, показывает его доброту... "
    "Это вроде и здорово, а вроде и не очень, ведь при нём я совершенно сама не своя. Немею, не могу ни слова сказать от всего потока тепла и нежности внутри, который будто циркулирует во мне. "
    "Однако, несмотря на всё моё беспокойство и одновременный восторг, усталость таки взяла своё, и я отключилась."
    window hide
    scene black with dissolve
    stop music fadeout 2
    window show
    br_un "Штайнкаутз... Странное название для Лагеря. Но вдруг мне там даже понравится?"
    jump exc_day1

#==========================================================================================================

label exc_day1:
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg 33_oldbus_int with dissolve
    play sound_loop sfx_bus_interior_moving fadein 2
    $ set_mode_nvl()
    "Новый, Венгерский и казалось, только что сошедший с конвеера Икарус рассекал бесконечные летние поля, двигаясь по дороге всё дальше на юг страны."
    "В каком-то смысле в голове не укладывалось, что случилось, ибо это было последнее, что я ожидала перед  тем, как отучиться последний год в школе. "
    "Теперь мы - пионервожатые. Мне никогда не приходилось работать с детьми… Да что уж там, я сама до сих пор в душе ребёнок. А Грета ещё больший ребёнок, чем я. Её легкомыслию и взгляду на жизнь может позавидовать любой человек, родившийся в тридцатые годы! Такое чувство, что возраст её совсем не меняет. Неужели в её жизненном опыте не было ничего такого, что перевернуло бы её мировоззрение и поменяло взгляд в сторону более взрослую? "
    "Впрочем, если его и не было, ей остаётся только позавидовать. Она познает очень многое в любом случае, но у неё это ещё впереди, и произойдёт это на более мирных и безобидных вещах…."
#Спрайты: 
#Брант отдельно, его взор всю дорогу был направлен в окно, а Грета сидела рядом.
    show br normal at fleft
    show gr normal at cright
    with dissolve
    $ renpy.pause(1.5, hard=True)
    "Её волосы были как золото, заплетённое в две большие косы, а глаза голубые, и казалось, что они были глубже океана. Грета одна из немногих людей, с которыми я могла общаться в школе и с кем имела хоть какой-то контакт. Она была общительной девушкой, хоть и училась не так уж и хорошо. Однако, например, на уроках труда ей не было равных, как и на физической подготовке. Ух, она не представляла себе утро без пробежки."
    "Она родилась 27 января, в 1936 году. Мы с ней были почти одного возраста, но при этом между взглядами на жизнь – пропасть. Впрочем, может именно поэтому мы и стали подругами? Противоположности притягиваются, в конце концов. "
    "Брант, насколько я помню, родился в 1936 году, кажется, 30 января. А я - 30 июня 1936 года."
    "Одногодки мы, в общем. Но была в Грете одна особенность, которая перечёркивала в ней все, и без того немногочисленные, минусы. Она не упускала никогда ни единой возможности помочь людям, по характеру была альтруисткой. Потому даже сейчас она посмотрела на меня и, подмигнув, указала жестом на Бранта, что сидел у окна и смотрел в него."
    "От одной мысли, что он поедет с нами, на моих щёках вспыхивал румянец, а мысли путались. Но Грета всегда подставляла мне \"моральное плечо\" в такие моменты, отчего мне становилось легче. Сейчас же она взяла меня за руку и спросила с улыбкой:"
    $ set_mode_adv()
#*текст внизу*
    gr_ddr "Ну?"
    un "Что?"
    gr_ddr "Придумала уже, как и когда скажешь ему? Нельзя же тянуть, Лена! Времени столько впереди, чем раньше скажешь, тем лучше."
    un "Грета! "

    "Я немного покраснела и уставилась в окно."
    gr_ddr "Ну чего ты? Зачем смущаться? Лучше вот соберись, давай и сделай это, - прошептала она. - Вон, сидит, тоже в окно пялится. Кто знает, о чём он думает? Вдруг о тебе?"
    "Щёки ещё сильнее запылали. Ей что, нравится это?!"
    un "Я... Обязательно подумаю. "
    "Всё-таки,  взгляд в окно помогает отвлечься. Меж тем поля и деревни сменились городским пейзажем..."
#*снова текст на весь экран.*
    $ set_mode_nvl()
    "Люди, что всё время спешат по своим делам... Памятники, вон идёт трамвай. Хи, пивнушки, как же без них? Всё было чисто, уютно и очень красиво. Мелкие детали, украшенные пёстрыми надписями, здания, наверняка подарившие сотням тысяч людей крыши над головой панельные дома и высотки, все это делает обычный город более живым. Живым..."
    "Это был послевоенный Дрезден. Я даже боюсь представить всю эту естественную красоту, лежащую в руинах. Правда говорят, что до того как его сравняли с землёй, город был ещё прекраснее и хранил множество памятников архитектуры. Но больше всего было как раз в домах, которым, порой, было сотни лет! Кто в них только не жил, и что эти стены могли только не видеть… А теперь всё это обратилось в прах, сгорело дотла вместе с людьми из-за бомб, что сжигали до основания всё живое и неживое… "
    "Вот что сделал социализм с этим разрушенным до основания городом. Воскресил его, подарил ему и его жителям новую жизнь. Дал возможность не закончить свой век в обломках и руинах, а обрести новую, социалистическую страницу своей истории. "
    nvl clear
    "Наконец каникулы, учёба позади!"
    "Делай всё, что хочешь, лето впереди..."
    "Без родителей впервые, уезжаешь ты,"
    "Кто тебе подскажет, как себя вести?"
    "Хорошее настроение у молодых ребят,"
    "Им слова напутствия мамы говорят,"
    "Лагерь это здорово, веселье там, любовь,"
    "Приключения и лето, зажгут твоё сердце вновь..."
    "Примерно так я переводила одну из, наверно, сотен песен, которые пели пионеры всю дорогу. Среди них попадались и русские, особенно им нравились \"взвейтесь кострами\". Ничего удивительного, Советские Пионеры посещали ГДР так же часто, как мы СССР и другие Советские Республики."
    nvl clear
   #======здесь что-то сделать для переключения персонажа 

    "Меняющиеся виды природы из окна могли вогнать меня в сон, да только теперь все мои мысли занимал город, который только мелькал перед моими глазами. Виды, менявшиеся в окне, были похожи на кинохронику, только покрашенную в цвета. Меня пробило удивление от первых же минут, как мы проезжали в нём."
    "Город… Он... Почти не выглядит разрушенным... Почему?"
    "Я ожидал увидеть его не таким, а как минимум в прежнем состоянии, то есть в руинах! "
    "Впрочем, если рассуждать чуть более логически, то этого следовало ожидать. Всего лишь вынужденная мера по его восстановлению, чтобы завоевать наше доверие, только и всего. Да и ехали мы, скорее всего, лишь по восстановленным улицам специально, чтобы нам не было видно разрушенных до основания кварталов."
    "Бомбардировка этого города длилась около двух дней (с 13 февраля по 15 февраля). Никто, ни один политик,  до сих пор не извинился за эти налеты. То, что произошло, ознаменовало падение Великой Германии. Уничтожена архитектура (соборы, музеи, здания парламента, жилые дома), и что самое ужасное погибли десятки тысяч мирных жителей."
    "Они обосновывают эти налеты местью! Наверняка  в мемуарах своих они об этом ни слова не скажут... Эта была война на уничтожение!"
    "Их песни... Не то, чтобы они раздражали, но и слушать их, а уж тем более подпевать не было никакого желания. Единственное желание, что у меня действительно было, так это одно: спать. Выехали мы довольно рано. Но даже несмотря на немаленькую скорость, которую развивал автобус по автобану, поездка, как мне кажется, длиться уже целую вечность."
    nvl clear
   #======здесь что-то сделать для переключения персонажа

    "Но внезапно поля сменились лесными массивами. Солнечные лучи теперь с трудом пробивались сквозь лесные ветки, и  тех, что сумели, хватало лишь на мгновение блеснуть подобно солнечному зайчику. "
    stop sound_loop fadeout 2
    "Наконец, показалась остановка.  Автобус остановился и распахнул двери."
    $ set_mode_adv()
    pi_ddr "Мы уже приехали? "
    un "Да, мы на месте – ответила я ему ласково. "
    gr_ddr "Соблюдайте дисциплину при выходе! Выходим по одному, не толкаемся! Один за другим, не толкаемся и не забываем свои вещи! "
    "Я постаралась подождать, когда большинство детей, толкаясь, не  выйдет из автобуса. Надоело поди сидеть на месте после долгой поездки. Когда в автобусе не было никого, кроме меня и Бранта, стеснение само буквально вытолкало меня на улицу... "
    scene white with dspr
    $ renpy.pause(0.3, hard=True)
    scene bg ddr_ext_camp_entrance_day with dspr
    $ set_mode_nvl()
    "Не успела я и шагу ступить на землю, как солнечный свет на секунду ослепил меня."
    "На меня смотрели статуи двух пионеров. Над воротами красовалась новая, будто только что сделанная, надпись \"Штаинкаутз\", а по бокам висели флаги с поочерёдно сменявшими друг друга чёрными, красными и жёлтыми цветов полосами. Название лагеря с немецкого, примерно переводилось как \"Совёнок\". Солнце было в самом-самом зените и одаривало землю июньским теплом. Небосвод был голубым, почти без единого облачка. Несмотря на всё летнее тепло, издалека ветер принёс водную прохладу."
    gr_ddr "Правда красиво? "
    "Грета, стоящая рядом, вывела меня из раздумий. "
    gr_ddr "Давай, Лена, нам нужно идти к администрации, чтобы получить назначение и заявить о своём прибытии!"
    "Только я собралась идти, как мимо меня прошёл Брант, держа свои вещи. Тут же прямо в меня врезается какой-то мальчик!" with vpunch
    "Вещи, что я держала у себя в руках, потянули меня вниз. Контроль над равновесием приближался к нулевой отметке!"
    un "Оооооой! "
    "Но тут кто-то буквально подхватил меня, удержавши от столкновения с асфальтом."
    br "Осторожнее, Лен. Расшибёшься ещё в первый же день... "
    play music music_list["two_glasses_of_melancholy"] fadein 3
    show br normal with dissolve # Брандт, эмоция: поза1нормал
    "Прозвучал неуверенный мужской голос. Рядом лежали и мои, и его вещи. Тело чувствовало чьи-то тёплые, сильные руки, на которых я в итоге, просто повисла, лишь для того, чтобы избежать столкновения с асфальтом!"
    "Сердце мгновенно заколотилось, и краснота на лице не заставила себя долго ждать."
    un "С-спасибо – лишь проговорила я, встав на землю и вернув себе равновесие."
    "Брант ничего не ответил, лишь побрёл дальше, даже не бросив на меня взгляда. Как будто ничего и не было..."
    $ set_mode_adv()
    
    "В глубине лагеря было не менее красиво, чем у ворот. Видно, что его возвели сравнительно недавно. На стене здания Администрации висела карта этого лагеря. Чего тут только не было… "
    scene bg ext_stage_normal_day with dissolve2
    "Сцена."
    scene bg ext_boathouse_day with dissolve2
    "Пристань." 
    scene bg ext_library_day with dissolve2
    "Библиотека." 
    scene bg ext_clubs_day with dissolve2
    "Kлубы…"

    scene bg black with dissolve2
    "После краткого разговора с директором лагеря, детей нужно было собрать около сцены. "
    scene bg ext_stage_normal_day with dissolve
    "Сцена была довольно неплохой, на ней даже стоял рояль. Вопрос только, кому на нём играть?  "
    "Включив микрофон, на сцену вошли мы и директор лагеря." 
    "Поприветствовав нас и детей речью,  он вручил Грете распределительный лист. Довольно предсказуемо, что я буду руководить девочками, а Брант парнями. И отрядов у нас будет по одному. Детей в этом году мало, потому что лагерь возведён сравнительно недавно и, по-хорошему, нуждается в расширении. Но всему своё время."
    "Директор лагеря на линейке выглядел довольно радостно. Это был мужчина лет 40, с небольшой бородой и очками. Было видно, что он уже не первый раз руководит подобными организациями."
    di_ddr "Данная смена должна запомниться вам на всю жизнь, и вы можете вынести из неё немало уроков для себя!"
    "Бла-бла-бла..."
    di_ddr "А теперь,  я вместе с вашими вожатыми лично покажу вам весь лагерь."
    un "Следуйте за мной. Не отставайте и не расходитесь."
    "Проговорила я, уже своему отряду. "
    "Собрав всех в группу, мы отправились на, можно сказать, экскурсию. "
    "Остальные полдня ушло на то, чтобы осмотреться."
    "Вот какие \"локации\" я для себя выделила, не считая сцены."
    scene bg ddr_ext_square_day with dissolve
    "Площадь."
    "Приятное место, с лавочками. Можно посидеть и прийти в себя, если там тихо. Центр \"украшает\" собой памятник партийному деятелю Эрнсту Тельману."
    scene bg ext_aidpost_day with dissolve
    "-Медпункт. "
    "Честно говоря, я ожидала чего-то более современного. Однако это было лишь первое впечатление. "
    scene bg int_aidpost_day with dissolve
    "Когда мы зашли внутрь, оказалось, что он вполне соответствует своему названию. Но говорили, что здесь главное в том, кто в нём работает."
    show cs smile with dissolve
    "Этим была наша медсестра, с… Довольно пышными формами. Однако, как сказали, дело своё она знает прекрасно и обладает высоким профессионализмом.  В общем, в случае чего, без медицинской помощи не останемся. "
    
    scene bg ddr_ext_storage_day with dissolve
    "-Склад."
    "Самый обычный склад.  В нём же нам, всем и каждому, и выдали униформы пионеров и вожатых соответственно. "


    show fr laugh at cleft
    show al base at cright
    with dissolve
    "Для пионеров это белая рубашка с синим галстуком и знаком \"seid bereit!\" (всегда готов!) на плече, а также синяя пилотка. Наша же форма, вожатых, имела небольшие отличия."
    "Она была полностью синей и без галстука, разумеется. На плече была эмблема FDJ \"Freie Deutsche Jugend\" (Союз свободной немецкой молодёжи), под эгидой которой мы с Брантом и Гретой и будем здесь вожатыми."
    "Лица многих детей выражали радость новой формой. Мне она также идеально подошла, чувствовались удобство и практичность, присущие всему немецкому."
    
    hide fr
    hide al
    with dissolve

    show sl angry pioneer at cleft
    show br angry at cright
    with dissolve
    "Бранту же она сначала была просто мала и не налезала, а та другая, что принесли, оказалась не глаженой. Грета выражала своё \"фи\", ибо, по её мнению, такая форма была \"старомодной\"."
    hide br
    hide sl
    with dissolve
    
    scene bg int_dining_hall_people_day with dissolve
    "-Столовая."
    "Ничего примечательного. Обычная столовая, мало отличающаяся от нашей школьной. Всё такие же стулья, столы, кафель на полах. И так же из неё нёсся заманчивый аромат."
    "В столовой нас и покормили первым, довольно вкусным, обедом."
    
    scene bg oldday1 with dissolve
    "-Помещение для вожатых."
    "Особенно занятное здание, в котором мы и будем жить, пускай оно и больше похоже на детский сад. Видно, что оно \"пострадало\" от войны, но лишь местами и то, лишь если хорошо приглядеться. Двухэтажное. Один, по идее, для девочек, другой для мальчиков."
    "Правда, нас было не настолько много, но сразу видно, что его строили \"на будущее\", когда в лагерь будет приезжать в разы больше детей и, соответственно, вожатых, чем сейчас. Как и над всеми зданиями, и около ворот, на нём были развешены  жёлто-красно-чёрные флаги ГДР."
    
    scene bg ext_library_day with dissolve
    "-Библиотека."
    "Чувствую, это будет моим любимым местом. Пускай на вид это самая обычная библиотека, но на деле те, кто руководил ею, позаботились о разнообразии книг на совесть. Ремарк, Кафка (не самое детское, но сюда должны ходить не только дети, но и мы, подавать им хороший пример), Шмитд, Югнер..."
    "Не обошлось и без идеологической литературы, её было не менее четверти. Также здесь хранились пока что немногочисленные, но всё же архивы лагеря."
    scene bg ext_boathouse_day with dissolve
    "-Пляж/пристань"
    "Рядом с лагерем текла речка, и была лодочная станция с пристанью. На вид вода была тёплая, и купаться здесь, я думаю, будет довольно приятно... Так, Лена! Не отвлекаться! Ты здесь не развлекаться пришла, а следить за детьми! "
    scene bg ext_clubs_day with dissolve
    "- Клубы."
    "Здание, больше похожее на обычные мастерские. Здесь особо талантливые дети будут мастерить всякое. Но пока что, там ничего нет. Оборудование подвезут позже, как нам сказали. Правда, сомневаюсь, что особенно талантливым будущим инженерам это помешает."
    scene bg ext_stage_normal_day with dissolve
    "- Сцена."
    "Та самая сцена, на которой мы сидели и слушали вступительную речь директора лагеря. Не совсем понятно, зачем нам показали её снова."
    "Может, это часть менталитета и для порядка надо показать в лагере всё-всё-всё? Ах да... Там было музыкальное оборудование, но для чего оно и откуда, мне предстояло узнать позже."
    scene bg ext_musclub_day with dissolve
    "- Художественная мастерская."
    "Весьма приятное на вид здание с большими стеклянными окнами. В самом здании было пусто, лишь стояли мольберты, но зайдя в кладовку, мы будто оказались в логове художника - были целые наборы красок, кистей, палитр... Для того, кто здесь работает, рисование - это нечто большее, чем просто набор красок, это целая жизнь."
    stop music fadeout 2
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ddr_ext_square_sunset with dissolve
    "Вот мы и обошли весь лагерь... Небо становилось золотистым."
    show sl smile pioneer with dissolve
    gr_ddr "Ну как тебе лагерь? "
    un "Очень нравится, думаю, время здесь провести можно будет просто здорово!"
    gr_ddr "Только не забывай, что ты не одна."
    "Ах да... Дети. Я даже не знаю их поимённо. Интересно, смогу ли я поладить с ними?"
    show sl normal pioneer with dissolve
    gr_ddr "Чего задумалась? О них же?"
    un "Научилась читать мысли?"
    gr_ddr "А с тобой и читать их особо не надо, всё на лице."
    un "Ну тебя!"
    gr_ddr "Да не ну! Ты хоть с детьми, а не с бумажной работой всю неделю."
    un "Разве у тебя нет своего отряда?"
    gr_ddr "Нет. Мне поручили исключительно работу с документами. "
    un "Хорошо тебе, наверно."
    gr_ddr "Неправда! Скукота смертная будет всю неделю! Думаю, это из-за недобора. Если бы девочек разделили между тобой и мной, отряды получились бы слишком маленькими."  
    un "Может, попробуешь поговорить с руководством? Вдруг передумают, или просто найдут ещё кого нового, для столь скучной работы? "
    gr_ddr "Да, я попробую сегодня. Ну да хватит обо мне? Придумала чего насчёт Бранта? "
    un "Неа… "
    gr_ddr "Я так понимаю, тебя пока не толкнёшь, не станешь. Что ж, \"толкаю\". Пригласи его поговорить сегодня вечером у пристани, например. Прогуляйтесь, тебе же хорошо будет! Заодно чего нового о нём узнаешь. "
    "Идея Греты была вроде и хорошей. Но в то же время я прекрасно понимала, что вот так просто взять и кого-то пригласить это непросто. Особенно для меня. Однако… Первые шаги-то надо делать, верно? Просто решиться и сделать это. "
    un "Хорошо, спасибо за совет. Я постараюсь. "
    hide sl with dissolve
    "Теперь нас снова направили на площадь для чего-то важного."
    $ set_mode_nvl()
    "Мы собрались всем лагерем на площади. Детей было не так уж и много. Впрочем, и сам лагерь был небольшого, пока что, размера. Уверена, в дальнейшем его могут и расширить."
    "Перед детьми стояли я, Грета, Брант и Директор Лагеря."
    di_ddr "Я очень надеюсь, что вы проведёте это время с пользой и обязательно научитесь чему-то новому..."
    "После весьма длинной речи..."
    di_ddr "Елена, прошу, зачитайте нашим гостям заповеди нашего лагеря."
    "Почему я чёрт возьми?! Их так много... Ладно, Лена, соберись. Прочти их с выражением, чтобы они их повторили... Вот и все. Ничего сложного."
    un "Мы, юные пионеры, любим нашу Германскую Демократическую Республику."
    "Пионеры и Грета сзади повторили мои слова. "
    un "Мы, юные пионеры, любим наших родителей."
    un "Мы, юные пионеры, любим мир во всём мире."
    un "Мы, юные пионеры, поддерживаем дружбу с детьми Советского Союза и всех стран мира."
    un "Мы, юные пионеры, прилежно учимся, мы аккуратны и дисциплинированы."
    un "Мы, юные пионеры, уважаем всех рабочих людей и всегда оказываем настоящую помощь."
    un "Мы, юные пионеры, хорошие друзья и помогаем друг другу."
    un "Мы, юные пионеры, с удовольствием поём и танцуем, играем и мастерим."
    un "Мы, юные пионеры, занимаемся спортом и заботимся о чистоте и здоровье нашего тела."
    un "Мы, юные пионеры, с гордостью носим синие галстуки."
    un "Мы готовимся стать пионерами-тельмановцами."
    "Почти всё. Вроде ничего сложного. Однако во время чтения я заметила лишь одну странность. В толпе я могла различить много голосов, пускай они и сливались между собой, ведь дети и вожатые говорили почти что хором. Но среди них я не могла различить столь важного для меня мужского голоса."
    "Странно, я вижу, как уголки рта Бранта двигаются, но я не слышу даже отголоска. Делает вид? С чего бы? Это довольно странно..."
    "Ладно, осталось чуть-чуть."
    nvl clear
    un "Примером нам служит Эрнст Тельман."
    un "Я, пионер-тельмановец, клянусь жить, учиться и бороться так, как учил нас Эрнст Тельман."
    un "Верный нашему девизу!"
    un "За мир и социализм!"
    un "Всегда готов!"
    "В последних словах звучал особый оптимизм и жизнерадостность, смешанный со смехом. Детей очень радовали такие слова клятвы. Меня тоже, по правде говоря. Но во всей этой бочке мёда была одна муха, которая мне не давала наслаждаться всем этим и вносила много сомнений."
    "Это молчание Бранта. Почему меня это так беспокоит?"
    $ set_mode_adv()
    scene bg ddr_ext_houses_sunset with dissolve
    "Пионеры жили в своих домиках. Их расселили по два человека, мальчик с мальчиком, девочка с девочкой. Дети быстро расположились в своих домах, хоть и начинали баловаться, вместо того, чтобы лечь спать. Такие проблемы больше были у Бранта, у него ведь группа мальчиков."
    "Наконец, весь мой отряд был благополучно уложен спать, и я уверена, что после столь насыщенного дня они спали достаточно крепко, чтобы не натворить дел. Фух, теперь можно и домой, хоть вещи разложить."
    show br normal with dissolve
    "По дороге мне встретился Брант, шедший в том же направлении."
    un "Ну что? Улеглись спать?"
    "Вид у него был уставший, однако увидев меня, он улыбнулся."
    br "Ха, почти что. Каким-то чудом их утихомирить удалось."
    un "Не очень ладишь с ними?"
    "Его взгляд малость забегал, после чего он быстро ответил:"
    br "С трудом."
    "Вот-вот дойдём до здания. Сейчас ещё не сильно темно, может быть... Волнение захлестнуло меня, от чего я остановилась. Давай Лена, это не так трудно!"
    un "Слушай..."
    br "Да?"
    "Повернулся он."
    un "Может... Встретимся у того причала?  Просто... Поговорим, воздухом подышим. Вот."
    "Сначала в его взгляде читалась небольшая растерянность."
    br "Хорошо, давай. Во сколько?"
    un "Да хоть... Через полчаса."
    br "Хорошо."
    "Улыбнувшись, я пошла с ним дальше. Скорее всего, я выгляжу как дура. Хватит краснеть уже!"
    
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg oldnight1 with dissolve
    "Зайдя в здание, мы разделились. Даже тут девочки спят на 2 этаже, а мальчики на первом."
    "Комната была довольно уютной. Быстро сложив все свои вещи, я открыла окно и плюхнулась на кровать. Привычно положив голову на подушку,  собралась побыть в покое. Но тут послышался стук в дверь, так и не давший мне насладиться вечерним затишьем и побыть наедине со своими мыслями."
    "На пороге стояла Грета."
    gr_ddr "Лен! Вниз давай! Тут совещание небольшое!"
    "Этого только не хватало. Ещё полчаса слушать какую-то занудную речь директора не было никакого желания. Мне хотелось только посидеть в покое под прохладным вечерним ветром, смакуя сегодняшнюю с Брантом встречу."
    un "Мне нужно хотя бы вещи свои распаковать..."
    gr_ddr "Сказали, что это срочно!"
    "Чёрт."
    un "Ох... Хорошо."
    gr_ddr "Бранта я уже предупредила, он тоже сейчас спустится."
    
    scene bg oldlag1_night with dissolve
    "Нас собрала Грета по поручению руководства, чтобы передать нам сообщение. Но на деле это оказалось очередной занудной речью."
    di_ddr "Я собрал вас здесь только для того, чтобы напомнить вам о всей полноте ответственности, что мы несём перед лагерем за наших \"подчинённых\". Мы обязаны обеспечить им эту неделю так, чтобы она навсегда им запомнилась. К счастью, чем занять их вам придумывать почти не придётся."
    di_ddr"Каждое утро у нас будет линейка, на которой будет оглашаться план на день. Также вы получите \"характеристику\" на своих подчинённых завтра же. Там будут их имена, фамилии и ещё некоторые сведения, чтобы вы уже заранее представляли себе их интересы. Данные сведения предоставлены нам их преподавателями из школы. Всё поняли?"
    "Мы с Брантом закивали."
    di_ddr "И ещё. Увы, Грета, но как бы я не старался, но ты всё равно будешь заниматься лишь бумажной работой. Твоё \"назначение\" не обсуждается. Думаю, это из-за временного кадрового дефицита…"
    "Грете лишь оставалось закатить глаза."
    gr_ddr "Не переживай, Лен. Мы будем видеться, но редко. Честно. Я обещаю."
    di_ddr "Посему, мы будем видеться, но редко. Честно. Я обещаю.  Ещё вопросы есть? Тогда спокойной всем ночи."
    "Наконец-то. И прошло как раз полчаса. Я окликнула Бранта, идущего...наверх?"
    un "Через пять минут?"
    br "Да, я помню, не переживай."
    
    window hide
    window show
    
    scene bg ext_boathouse_night with dissolve
    "Вроде и ничего такого в этом нет. Обычная встреча парня и девушки на речной пристани. Однако для меня это так волнующе, ведь до этого я ни разу не могла позвать его вот просто так. Хотя бы потому что у меня банально не было времени. Так уж получилось, что расписание всегда было очень плотным."
    "Сначала основные уроки, а за ними начинается вторая школа – художественная. И заканчивалась она вечером. К тому же, загрузка заданиями была так тоже приличная. Вот и получается, что у меня почти все мысли были лишь об учёбе либо там, либо сям. И лишь иногда как \"лучик\" света во всей этой тьме дел и забот была мысль о нём."
    "Этот прилив тепла в моей груди, который затем растекался по всему телу, давал мне как физических, так и творческих сил. Интересно, он хоть один раз, хоть на секундочку, думал о том, что лишь одна мысль о нём может вдохнуть в кого-то новые силы?"
    "Поэтому я с таким нетерпением ждала этого... Было и радостно, и страшно одновременно."
    "Так... Нужно расслабиться и успокоиться. Вдыхаю вечерний, смешанный со свежестью воды воздух всей грудью. Пытаюсь собраться с мыслями, заранее как-то всё продумать. Да всё равно не по себе! А вдруг что-то пойдёт не так?! Скажу опять какую-то ерунду, спугну ещё... Ладно, выдохнула я. Будь что будет." 
    "Тело опрокинулось на живот и пальцы начали рассекать водную гладь, пуская небольшие волнения. Как и ожидалось, вода довольно тёплая. Может, даже получится искупаться. Детишкам уж точно, по крайней мере. "
    "В отражении воды были лишь моё задумчивое лицо и рука. Вода приятно колыхалась небольшими волнами от ветра и моих пальцев. "
    "Но наконец, моё отражение в воде кто-то дополнил. "
    br "Смотри не упади."

    scene cg 321-vosstanovleno with dissolve
    play music music_list["waltz_of_doubts"] fadein 3
    "Я лишь улыбнулась в ответ. Он присел рядом и тоже посмотрел вдаль, как и я. Мы не решались друг на друга посмотреть."
    "Звуки уже почти ночной природы окутали нас, погрузив в молчание, от которого становилось довольно-таки неловко. Надо было это разрушить хоть как-то..."
    un "Тебе нравится здесь? И... Как твой отряд? "
    br "Бравых пионерят?"
    un "Хи, почему так?"
    br "Да не знаю, с ними трудно. Я никогда не работал с детьми вообще.  Непослушные они..."
    un "А как тебе это место? Город?"
    "Он поначалу задумался. А мне в голову снова закралось то самое сомнение. Оно как червь в яблоке: медленно прогрызало во мне тоннели, которые порождают неприятное и противное недоверие. Ладно, хватит преувеличивать, мне могло вовсе показаться."
    br "Город приятный, совсем не таким ожидал его увидеть. А лагерь... Здесь спокойно и тихо. По правде говоря, я думал, что будет хуже. Гораздо."
    un "Почему?"
    "Он промолчал. Снова повисла неловкая тишина. В этот раз нарушить её решился он."
    br "Вообще-то, Лен, я рад, что ты и Грета здесь. Без вас было бы... Одиноко."
    "Вот тут я уже не могла сдержать глупой, как мне кажется, улыбки. Ну хоть щёки под контролем... От его ответа, как от сердца отлегло. Значит, он всё-таки нормально относится к нам с Гретой. Подумать только, как я могла то подумать о ином? "
    "Вновь неловкая пауза. Терпеть не могу это. Как вдруг мне в лицо прилетела прохладная вода. Я посмотрела на его довольное лицо."
    un "Ах ты!"
    "Ответный плеск уже ему в лицо. И попрошу заметить, он был гораздо крупнее предыдущего. Пришлось сесть как он и окунуть ноги в воду. Взаимные барахтанья ногами принесли своё и мы были наполовину мокрые."
    "Посмотрев друг на друга в столь неловкой ситуации, мы рассмеялись."
    un "Думаю, нам пора. А то злиться будут."
    br "Да, хороший душ перед сном… "
    "Мы, снова рассмеявшись, и пошли в сторону домиков. Ну, точнее, пошла только я. Он же свернул куда-то в сторону пляжа. Пойти ли с ним? Впрочем, может, он хочет побыть один? Пускай идёт, сама понимаю его. К тому же на тело напала безумная усталость."
    stop music fadeout 2
   #======здесь что-то сделать для переключения персонажа   
    scene bg ext_beach_night with dissolve
    $ set_mode_nvl()
    "Голубая небесная гладь начала постепенно приобретать розовые оттенки садящегося солнца. Пляж сегодня был пустой, ибо в первый же день детям никто купаться не даст. Было бы здорово, если бы такое разрешили нам, но увы."
    "Место вроде хорошее, тут тихо и спокойно. Жаль, отчасти, что скоро эту тишину будут постоянно сотрясать детские вопли, а спокойствие самым наглым образом разрушать разного рода забияки, на которых ещё  именно тебе нужно находить какую-то управу. По-моему, тут гораздо лучше находиться в качестве отдыхающего, но никак не \"вожатого\"."
    "Но в целом, мне тут всё равно нравится. Пускай и с меньшей пользой для себя, но всё-таки отдохну. Перед глазами на мгновение показалась наша с Леной \"беседа\" на пристани недалеко отсюда. Да, хорошая она всё-таки. Как и Грета. Я правду ей сказал, что без них было бы одиноко."
    "Я лёг на песок, и мой взор обратился к небу. А при взгляде туда в голову лезло всё больше мыслей."
    "Дрезден. Восстановлен, несмотря на  то, что во время войны его, по сути, стёрли с лица земли. Это место, я уверен, тоже пострадало очень сильно. И всё это отстроили мы сами, немцы. Несмотря на то, что вторая, и, видимо, последняя для нашего народа война со всем миром с треском проиграна. Но это не мешает нам восстанавливаться из руин."
    "Что большего всего меня удивляет, так это то, что, казалось бы, обозлённые на нас русские, оккупировав нас и \"расчленив\" на части (ибо разделяй и властвуй), должны камня на камне от нас не оставить и не давать ни малейшей возможности восстановиться в знак наказания."
    "Может, я всё же сильно-сильно не прав в своём отношении к этому всему? Может, мой отец всё-таки прав? И почему я раньше просто не думал, а просто заперся буквально в коконе собственных переживаний и, частично, ненависти, даже не пытаясь выглянуть из него и оценить реальное положение дел?"
    "Нас не морят голодом, учиться дают, даже в такие хорошие места отправляют задаром. Даже отца моего пощадили, несмотря на то, что он..."
    nvl clear
    "Зря я всё же накричал на него тогда. Вёл себя как чёрт знает кто. Как вернусь, я обязательно извинюсь перед ним."
    "Правда, эту их \"клятву\" всё же давать не стал. Лично для себя я сделал правильно. Не из-за ненависти к этому всему, уже не из-за этого. Нельзя клясться в том, во что ты не веришь всей своей душой, сердцем и телом. А я ещё не настолько \"верю\" во всё это, чтобы клясться. Поэтому, я хоть и смухлевал, зато не стал лицемером. Да и есть всё же некоторые вещи, за что я презираю эту коммунистическую оккупацию."
    "Мама. Эх, она на \"другой стороне\" осталась. Этого не отнять. Как же я давно её не видел..."
    "Залез  в карман и развернул небольшую фотографию. Всегда ношу её с собой, чтобы не забыть хотя бы внешность. Её же нежный голос постепенно стирается из моей памяти. Увидеть бы её снова..."
    $ set_mode_adv()
    "Ладно, рано делать выводы. Несмотря на всё хорошее, меня всё равно что-то тревожит. Как будто всё происходит не просто так. Надо бы возвращаться в здание для вожатых, темнеет уже."
    scene bg ddr_ext_houses_night with dissolve
    "На лагерь опустилась ночь. Идя спокойно, но осторожно, я направлялся к дому для вожатых. Ночной ветерок приятно обдувал лицо и близлежащие кусты с деревьями. Всё же проведённое с ней время мне было более чем приятным. Я даже невольно поймал себя на мысли, что она мне..."
    "Приятно с ней. Да..."
    window hide
    scene bg oldnight with dissolve2
    $ renpy.pause(0.5, hard=True)
    scene bg oldnight1 with dissolve2
    window show
    "Оказавшись, наконец, в постели, я был готов к \"провалу\" в сон. Но перед этим в голове всё же пронёсся ответ \"да\". Это был ответ на мой вопрос, \"а понравится ли мне здесь?\"."
















return
    