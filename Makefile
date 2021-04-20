NAME		=		trade

SRC			=		trade.py

RM 			=		rm -f

all:
		cp $(SRC) $(NAME)
		chmod 777 $(NAME)

clean:
		@echo "Clean"

fclean:
		$(RM) $(NAME)

re:
		fclean all

.PHONY: all re clean fclean
