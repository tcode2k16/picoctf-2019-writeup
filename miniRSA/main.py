import gmpy2

n = 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e = 3
c = 2205316413931134031074603746928247799030155221252519872649651160278476902145087143487410518148797849017656369316341655241171591967799156330520717647775870050832989405039500714403825189288474886866683126666398914647066914847128627018357093 

gmpy2.get_context().precision=2000
print gmpy2.root(c,e)


print (hex(13016382529449106065894479374027604750406953699090365388202878069532790348997757)[2:-1]).decode('hex')

# picoCTF{n33d_a_lArg3r_e_6eb35d6d}