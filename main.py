

printf("エンターキーを押すと計測開始");
	getchar();
	start = clock();
	printf("エンターキーを押すと計測を終了します");
	getchar();
	end = clock();

	printf("%.2f秒です。\n", (double)(end - start) / 1000);



int main(void){

    int sauna1;
    int sauna2;
    int sauna3;
    int sauna4;
    int sauna5;

	clock_t start, end;

    printf("5個の項目を入力\n");
	printf(" 一回目の時間：");	scanf("%d", &sauna1);	
	printf(" 二回目の時間：");	scanf("%d", &sauna2);	
	printf(" 三回目の時間：");	scanf("%d", &sauna3);	
	printf(" 四回目の時間：");	scanf("%d", &sauna4);
    printf(" 五回目の時間：");	scanf("%d", &sauna5);

    
    
    
    if(sauna1==0||sauna2==0||sauna3==0||sauna4==0||sauna5 == 0){
        printf("判定できません");

    }

    else 
        printf("おｋ\n");

        return 0;

}



	printf("エンターキーを押すと計測開始");
	getchar();
	start = clock();
	printf("エンターキーを押すと計測を終了します");
	getchar();
	end = clock();

	printf("%.2f秒です。\n", (double)(end - start) / 1000);

    return 0;
    
}

	