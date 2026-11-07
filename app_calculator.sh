#!/bin/bash
if [[ $# -ne 2 || -z $1 || -z $2 ]]; then
    echo "Ошибка: не переданы аргументы" >&2
    exit 1
fi
num1=$1
num2=$2
echo "Сумма: $((num1 * num2))"
