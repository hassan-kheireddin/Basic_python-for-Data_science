# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkheired <hkheired@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 14:02:41 by hkheired          #+#    #+#              #
#    Updated: 2025/03/10 14:02:44 by hkheired         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    obj = type(object)
    if obj == list:
        print(f"List : {type(object)}")
    elif obj == tuple:
        print(f"Tuple : {type(object)}")
    elif obj == set:
        print(f"Set : {type(object)}")
    elif obj == dict:
        print(f"Dict : {type(object)}")
    elif obj == str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42
