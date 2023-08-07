from GUI import init_main_window, init_top_panel, init_shopper_page_frame


# Mainloop of SHOPPER application
if __name__ == "__main__":
    # Objects Initialization
    root = init_main_window()
    init_top_panel(root)
    init_shopper_page_frame(root)

    root.mainloop()
