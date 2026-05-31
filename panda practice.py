{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 25115,
     "status": "ok",
     "timestamp": 1779030304570,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "SDoIdF60SwYb",
    "outputId": "537cc2c5-c2d2-46ca-827f-c9650b99141f"
   },
   "outputs": [],
   "source": [
    "from google.colab import drive\n",
    "drive.mount('/content/drive')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 408,
     "status": "ok",
     "timestamp": 1779030307928,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "pNm90wJiYsBk",
    "outputId": "9434d1f6-713a-407a-cfc1-2d577c0a341e"
   },
   "outputs": [],
   "source": [
    "!ls \"/content/drive/MyDrive/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 206
    },
    "executionInfo": {
     "elapsed": 585,
     "status": "ok",
     "timestamp": 1779030310789,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "W7BoVRcpTiXA",
    "outputId": "69248d8b-39ce-4a35-d0dc-24cae00c299e"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('/content/drive/MyDrive/Copy of BikeIndia.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 676
    },
    "executionInfo": {
     "elapsed": 67,
     "status": "ok",
     "timestamp": 1779030314230,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "0WLcxIZiTnT5",
    "outputId": "a06a9d04-1130-40e2-df19-fd03f4e0d7b7"
   },
   "outputs": [],
   "source": [
    "df.head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 26,
     "status": "ok",
     "timestamp": 1779030358026,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "GRWKNxTqeNF_",
    "outputId": "54ee3c9d-77b2-496b-aaef-421e07c5ed91"
   },
   "outputs": [],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 320
    },
    "executionInfo": {
     "elapsed": 75,
     "status": "ok",
     "timestamp": 1779030401809,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "tNrL3Hq9eNOt",
    "outputId": "995b9872-50f7-430e-c0d5-ad8c486813fd"
   },
   "outputs": [],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 203
    },
    "executionInfo": {
     "elapsed": 79,
     "status": "ok",
     "timestamp": 1779030482127,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "6i9ENP36eNUY",
    "outputId": "872f5789-2630-42f8-8733-16c5aac63a71"
   },
   "outputs": [],
   "source": [
    "type(df[['yr']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 206
    },
    "executionInfo": {
     "elapsed": 21,
     "status": "ok",
     "timestamp": 1779030618157,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "D_iiPeLKe145",
    "outputId": "eeb2fe10-17f4-4180-a124-ae4c6b64b02f"
   },
   "outputs": [],
   "source": [
    "df.loc[2:6,['windspeed','registered']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "iUI5AYXoe19N"
   },
   "outputs": [],
   "source": [
    "df.set_index('instant',inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 237
    },
    "executionInfo": {
     "elapsed": 66,
     "status": "ok",
     "timestamp": 1779030927077,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "49zhJz9he2A1",
    "outputId": "3f300359-f737-4931-9930-57f77c290916"
   },
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 237
    },
    "executionInfo": {
     "elapsed": 77,
     "status": "ok",
     "timestamp": 1779031143242,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "SrsjMjoEe2EY",
    "outputId": "b3b59c2e-c54d-4de9-e8f5-9e130e87e3c1"
   },
   "outputs": [],
   "source": [
    "df.loc[2:6,['windspeed','registered']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 423
    },
    "executionInfo": {
     "elapsed": 64,
     "status": "ok",
     "timestamp": 1779031163692,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "fgsavW_ve2HR",
    "outputId": "05f05868-fc55-423d-d3a0-7d2e92209457"
   },
   "outputs": [],
   "source": [
    "df.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 237
    },
    "executionInfo": {
     "elapsed": 72,
     "status": "ok",
     "timestamp": 1779031758631,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "Cwp1eGQDhaU4",
    "outputId": "bb095b2b-6e9a-4ef1-ecc7-735226caba12"
   },
   "outputs": [],
   "source": [
    "df2 = df[df['windspeed']>10][['windspeed','atemp','temp','hum']]\n",
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 455
    },
    "executionInfo": {
     "elapsed": 46,
     "status": "ok",
     "timestamp": 1779032610509,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "eTNCiVpWhajl",
    "outputId": "71f10f52-b091-4bc6-a309-3648a35cdc52"
   },
   "outputs": [],
   "source": [
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 14,
     "status": "ok",
     "timestamp": 1779031794432,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "EzrgAKjohaY5",
    "outputId": "71d2a826-50db-47dc-e132-508f51462fd0"
   },
   "outputs": [],
   "source": [
    "df2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 29,
     "status": "ok",
     "timestamp": 1779032988700,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "1mDuT5G5hanP",
    "outputId": "a458d3cc-faf4-4cda-8cc5-0f3c8835692a"
   },
   "outputs": [],
   "source": [
    "df3 = pd.merge(df,df2,how='inner',on= ['temp','atemp'])\n",
    "df3.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "mEO7YQkVod3G"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 423
    },
    "executionInfo": {
     "elapsed": 70,
     "status": "ok",
     "timestamp": 1779032993454,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "zmSBopqQharu",
    "outputId": "12205a4f-1bb9-4bf6-f43d-b21846521029"
   },
   "outputs": [],
   "source": [
    "df3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 455
    },
    "executionInfo": {
     "elapsed": 56,
     "status": "ok",
     "timestamp": 1779032206279,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "4O7AKBsPlRoI",
    "outputId": "662d9a1d-03e7-414c-cbdb-42c89671c66b"
   },
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 42,
     "status": "ok",
     "timestamp": 1779033004854,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "PnXgKEKolRzv",
    "outputId": "2ecaab98-0650-4583-969e-be4f9ad64fed"
   },
   "outputs": [],
   "source": [
    "df3.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "PJbLbL7jlR32"
   },
   "outputs": [],
   "source": [
    "df4=pd.concat(axis=0,objs=[df,df2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 49,
     "status": "ok",
     "timestamp": 1779033153194,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "52LU1cWeogYW",
    "outputId": "b6807110-95fd-4f81-a8d7-a337d0b99408"
   },
   "outputs": [],
   "source": [
    "df4.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "5zy2-5PIogl_"
   },
   "outputs": [],
   "source": [
    "df['count_2']= df['cnt'].apply(lambda x: x*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 455
    },
    "executionInfo": {
     "elapsed": 60,
     "status": "ok",
     "timestamp": 1779033261929,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "zNKGtobdlR7P",
    "outputId": "5e1374f5-cda3-4dbd-84a8-8ba4f9cc6ce6"
   },
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "uIhSpXbepc4C"
   },
   "outputs": [],
   "source": [
    "df['s'] = df['dteday'].astype('str')+ \": \" + df['cnt'].astype('str')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 455
    },
    "executionInfo": {
     "elapsed": 82,
     "status": "ok",
     "timestamp": 1779033372885,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "xYIOTFbCpdF_",
    "outputId": "a6df9333-c1ab-4dc7-fca4-2d81191ec6c5"
   },
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "bmiNZFiEpw6J"
   },
   "outputs": [],
   "source": [
    "df.drop(['count_2','s'],inplace=True,axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 455
    },
    "executionInfo": {
     "elapsed": 52,
     "status": "ok",
     "timestamp": 1779033484675,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "2vSBSYnIpxDF",
    "outputId": "b8bbc949-b9a5-4e9a-c296-c53ed1151421"
   },
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a9665900"
   },
   "source": [
    "### `corr()` function explanation\n",
    "\n",
    "-   **Purpose**: Calculates the correlation coefficient between numerical columns.\n",
    "-   **Output**: Returns a correlation matrix, where each cell `(i, j)` represents the correlation between column `i` and column `j`.\n",
    "-   **Methods**: By default, it uses Pearson correlation. Other methods like Kendall and Spearman can also be specified.\n",
    "\n",
    "Let's see the correlation matrix for our `df` DataFrame:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 664
    },
    "executionInfo": {
     "elapsed": 98,
     "status": "ok",
     "timestamp": 1779033735604,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "4a2bac76",
    "outputId": "b23bd1cc-0ec8-46d8-de58-7121c5bc845b"
   },
   "outputs": [],
   "source": [
    "df.corr(numeric_only=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 363
    },
    "executionInfo": {
     "elapsed": 56,
     "status": "ok",
     "timestamp": 1779035899112,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "dpLVw30Lypbo",
    "outputId": "1877621a-a4fb-47d3-afbb-ed2b4d41e846"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}\n",
    "\n",
    "labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n",
    "\n",
    "d = pd.DataFrame(data=data,index=labels)\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 19,
     "status": "ok",
     "timestamp": 1779035960457,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "3apV9RNRypfX",
    "outputId": "402ba3f7-80b0-4385-8c67-3e503a986e07"
   },
   "outputs": [],
   "source": [
    "d.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 112
    },
    "executionInfo": {
     "elapsed": 38,
     "status": "ok",
     "timestamp": 1779035984504,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "E8DRHIqlypj0",
    "outputId": "9b626a96-ce1e-4366-b1ee-48db17bf6864"
   },
   "outputs": [],
   "source": [
    "d.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 363
    },
    "executionInfo": {
     "elapsed": 35,
     "status": "ok",
     "timestamp": 1779036070995,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "ZecjqPLzypnc",
    "outputId": "b80145d0-6012-4ab4-b983-eea9353e5f0c"
   },
   "outputs": [],
   "source": [
    "d[['birds','age']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 143
    },
    "executionInfo": {
     "elapsed": 77,
     "status": "ok",
     "timestamp": 1779036278063,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "668eoHP2ypq0",
    "outputId": "1825cfb1-2f76-46a5-9821-a58cf9bfa916"
   },
   "outputs": [],
   "source": [
    " #select [2, 3, 7] rows and in columns ['birds', 'age', 'visits']\n",
    "d.loc[['b','c','g'],['birds', 'age', 'visits']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 269
    },
    "executionInfo": {
     "elapsed": 29,
     "status": "ok",
     "timestamp": 1779036331931,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "kpSe9VfW037N",
    "outputId": "7ddd2686-9d6a-4bdc-c431-3e3bab779b11"
   },
   "outputs": [],
   "source": [
    "#select the rows where the number of visits is less than 4\n",
    "d[d['visits']<4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 112
    },
    "executionInfo": {
     "elapsed": 83,
     "status": "ok",
     "timestamp": 1779036917993,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "ggQpLCyB04Eu",
    "outputId": "0d108932-cdc5-4d93-d324-008d32c126c3"
   },
   "outputs": [],
   "source": [
    "d[np.isnan(d['age'])][['birds','visits']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 167
    },
    "executionInfo": {
     "elapsed": 37,
     "status": "ok",
     "timestamp": 1779037092104,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "Dd_BPaz404NF",
    "outputId": "9c50904c-a8af-4289-8310-6881030c73d8"
   },
   "outputs": [],
   "source": [
    "# Select the rows where the birds is a Cranes and the age is less than 4\n",
    "d[d['birds']=='Cranes'][d['age']<4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 175
    },
    "executionInfo": {
     "elapsed": 57,
     "status": "ok",
     "timestamp": 1779037387193,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "NPKxWvDh4CKo",
    "outputId": "b86fffb5-e0d9-4236-e46c-e78bb83b1957"
   },
   "outputs": [],
   "source": [
    "#Select the rows the age is between 2 and 4(inclusive)\n",
    "d[(d['age'] >= 2) & (d['age'] <= 4)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 18,
     "status": "ok",
     "timestamp": 1779037484442,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "GHWIFrfr4CPd",
    "outputId": "e803d4b5-f765-4e04-c2e7-c030f217e6fe"
   },
   "outputs": [],
   "source": [
    "#Find the total number of visits of the bird Cranes\n",
    "d[d['birds']=='Cranes']['visits'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 209
    },
    "executionInfo": {
     "elapsed": 57,
     "status": "ok",
     "timestamp": 1779037796840,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "F8VpgSUM4CT1",
    "outputId": "d130eeaa-d18e-4975-bfa2-0764d86391a1"
   },
   "outputs": [],
   "source": [
    "#Calculate the mean age for each different birds in dataframe.\n",
    "d.groupby('birds')['age'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 363
    },
    "executionInfo": {
     "elapsed": 67,
     "status": "ok",
     "timestamp": 1779037984469,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "f926a1af",
    "outputId": "93bed893-7fb3-4bdc-bf22-7ce2da39cb8e"
   },
   "outputs": [],
   "source": [
    "#Append a new row 'k' to dataframe with your choice of values for each column. Then delete that row to return the original DataFrame.\n",
    "d['nw']=d['age'].apply(lambda x: x*2)\n",
    "d.drop('nw',axis=1,inplace=True)\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 209
    },
    "executionInfo": {
     "elapsed": 42,
     "status": "ok",
     "timestamp": 1779038171659,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "y6bPk5XV4CXv",
    "outputId": "cb386059-6a5a-4aeb-8400-ab1c0ab8c7a7"
   },
   "outputs": [],
   "source": [
    "#Find the number of each type of birds in dataframe (Counts)\n",
    "d.groupby('birds').size()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 363
    },
    "executionInfo": {
     "elapsed": 46,
     "status": "ok",
     "timestamp": 1779038462732,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "Ty6MK_j28JAw",
    "outputId": "cdf96ddf-ac6c-4fac-8af6-058750eb4838"
   },
   "outputs": [],
   "source": [
    "#Sort dataframe (birds) first by the values in the 'age' in decending order, then by the value in the 'visits' column in ascending order.\n",
    "d.sort_values(by=['age','visits'],ascending=[False,True])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 363
    },
    "executionInfo": {
     "elapsed": 64,
     "status": "ok",
     "timestamp": 1779038741515,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "yGDAQYqq8JEj",
    "outputId": "ad5190f1-7ddd-48c1-b4ee-66e420f1efae"
   },
   "outputs": [],
   "source": [
    " #Replace the priority column values with'yes' should be 1 and 'no' should be 0\n",
    "d.loc[d['priority'] == 'yes', 'priority'] = 1\n",
    "d.loc[d['priority'] == 'no', 'priority'] = 0\n",
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 363
    },
    "executionInfo": {
     "elapsed": 53,
     "status": "ok",
     "timestamp": 1779038897392,
     "user": {
      "displayName": "Sampa Bandyopadhyay",
      "userId": "17306980934569768052"
     },
     "user_tz": -330
    },
    "id": "kykkaRr88JIe",
    "outputId": "0846fc68-f1cf-474a-f21a-abf9b5f64abd"
   },
   "outputs": [],
   "source": [
    "#In the 'birds' column, change the 'Cranes' entries to 'trumpeters'.\n",
    "d.loc[d['birds']=='Cranes','birds']='trumpeters'\n",
    "d"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyOxSCo3rXeFgGSn9s7xGtk1",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
