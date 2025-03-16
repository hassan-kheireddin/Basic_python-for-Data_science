# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkheired <hkheired@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 14:02:53 by hkheired          #+#    #+#              #
#    Updated: 2025/03/10 14:02:54 by hkheired         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

temp = sys.argv
try:
    if len(temp) == 1:
        sys.exit()
    try:
        if len(temp) != 2:
            raise AssertionError("more than one argument is provided")
        val = int(temp[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit()
if  val % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
