#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, items, coins):
        self.num_items = items
        self.item_coins =coins

    def buy(self,items,coins):
        if(self.num_items>=items and coins>=items*self.item_coins):
            self.num_items=self.num_items-items
            return coins-items*self.item_coins
        elif(self.num_items<items):
            print("not enough items")
            return 0
        elif(coins<=items*self.item_coins):
            print("not enough coins")
            return 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items,num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")

    fptr.close()