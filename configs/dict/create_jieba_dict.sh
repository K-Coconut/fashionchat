cat entity/* |tr "\t" "\n"  |sed 's/ //g'|dos2unix|awk '{print length($0)"\t"$0}'|sort -t$'\t' -r -k1 |awk -F"\t" '{print $2"\t"$1*10000000}' > jieb_dict/cut_dict
