cat entity/* |tr "\t" "\n"  |sed 's/ //g'|awk -F"\t" '{print $1"\t"10000000}' > jieb_dict/cut_dict
