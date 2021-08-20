{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyM3JwuG6i6efx2QlKH0YV7W",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/marcelohenrique15/studying-python/blob/main/input.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Oa9JRU9ukCb",
        "outputId": "e19e9e2e-ea85-4ce4-a7be-e2d94745f027"
      },
      "source": [
        "nome_aluno = input(\"Digite seu nome e sobrenome:\")\n",
        "idade_aluno = input(\"Digite sua idade:\")\n",
        "escola = input(\"Digite o nome de sua escola:\")\n",
        "nota1 = input(\"Digite a sua nota da primeira unidade:\")\n",
        "nota2 = input(\"Digite a sua nota da segunda unidade:\")\n",
        "nota3 = input(\"Digite a sua nota da terceira unidade:\")\n",
        "nota1 = float(nota1)\n",
        "nota2 = float(nota2)\n",
        "nota3 = float(nota3)\n",
        "soma_notas = nota1 + nota2 + nota3\n",
        "media = soma_notas/3\n",
        "\n",
        "print(\"Seu nome é\", nome_aluno, \", estudante do\", escola)\n",
        "print(\"Você tem\", idade_aluno, \"anos.\")\n",
        "print(\"Sua média é\", media)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Digite seu nome e sobrenome:Marcelo Henrique \n",
            "Digite sua idade:17\n",
            "Digite o nome de sua escola:IFPE\n",
            "Digite a sua nota da primeira unidade:8\n",
            "Digite a sua nota da segunda unidade:9\n",
            "Digite a sua nota da terceira unidade:10\n",
            "Seu nome é Marcelo Henrique  , estudante do IFPE\n",
            "Você tem 17 anos.\n",
            "Sua média é 9.0\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}