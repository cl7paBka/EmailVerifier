from colorama import Fore, Style, init


def colored(word, colorama_func):
    return f"{colorama_func}{word}{Style.RESET_ALL}"


def print_logo():
    logo = (r"""
     /\_/\                   /\_/\ 
    ( o.o )                 ( o.o )
     > ^ <                   > ^ <"""
            + f"""
    ###############################
    # -#                        #-#
    #  -#    {colored('EmailVerifier', Fore.MAGENTA)}    #-  #
    #    -#   {colored("by cl7paBka", Fore.MAGENTA)}   #-    #
    #      .#             #.      #
    #        .#         #.        #     
    #          .#     #.          #
    #        -#  .# #.  #-        #
    #      ##             ##      #
    #   +#                   #+   #
    # ##                       ## #
    ###############################
    """)

    print(logo)

    return ''
