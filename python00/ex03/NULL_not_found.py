# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkheired <hkheired@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 14:02:47 by hkheired          #+#    #+#              #
#    Updated: 2025/03/10 14:02:48 by hkheired         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:

    if object == None:
        print(f"Nothing: {object} {type(object)}")
    elif type(object) == float and object != object:
         print(f"Cheese: {object} {type(object)}")
    elif object == 0 and type(object) == int:
         print(f"Zero: {object} {type(object)}")
    elif object == "":
         print(f"Empty: {object} {type(object)}")
    elif object == False and type(object) == bool:
         print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
