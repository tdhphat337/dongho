try:
    import pygame
    from datetime import datetime

    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    PINK = (255, 192, 203)

    # define screen size
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 300

    # initialize pygame
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    pygame.display.set_caption("Clock")

    # define font
    font = pygame.font.SysFont("comicsansms", 50)

    # define reset button
    reset_button = pygame.Rect(10, 10, 80, 30)

    # define set timer button
    set_timer_button = pygame.Rect(100, 10, 100, 30)

    # define timer font
    timer_font = pygame.font.SysFont("comicsansms", 40)
    # define timer variables
    timer_active = False
    timer_start = None
    timer_length = 0

    # define sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound("file.mp3")
    def draw_clock():
        # get current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %p")
        
        # draw background
        screen.fill(PINK)
        
        # draw time
        font = pygame.font.SysFont("comicsansms", 50)
        text = font.render(current_time, True, YELLOW)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
        
        # draw reset button
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("Reset", True, WHITE)
        reset_button = text.get_rect(center=(50, 20))
        pygame.draw.rect(screen, YELLOW, reset_button, 2)
        screen.blit(text, reset_button)
        
        # draw set timer button
        text = font.render("Set Timer", True, WHITE)
        set_timer_button = text.get_rect(center=(120, 20))
        pygame.draw.rect(screen, YELLOW, set_timer_button, 2)
        screen.blit(text, set_timer_button)
    def reset():
        draw_clock()
    def set_timer():
        # get user input for timer
        minutes = input("Enter minutes: ")
        seconds = input("Enter seconds: ")
        
        # convert input to integer
        minutes = int(minutes)
        seconds = int(seconds)
        
        # calculate total seconds
        total_seconds = minutes * 60 + seconds
        
        # start timer
        pygame.time.set_timer(pygame.USEREVENT, total_seconds * 1000)
        
        # draw timer
        draw_clock()
    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                print("Timer done!")
                sound.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check if Reset button clicked
                if reset_button.collidepoint(event.pos):
                    reset()
                # check if Set Timer button clicked
                elif set_timer_button.collidepoint(event.pos):
                    set_timer()
        
        # draw clock
        draw_clock()
        
        # update screen
        pygame.display.update()

    # quit pygame
    pygame.quit()
except Exception as bug:
    print(bug)