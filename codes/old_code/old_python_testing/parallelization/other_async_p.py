import asyncio
import subprocess
from datasets import load_dataset, parallel

async def run_subprocess(val):
    command = ['clang','-O3','-c','-xir','-o','-','-']
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE
    )

    stdout, stderr = await process.communicate(input=val)


async def main():
    with parallel.parallel_backend('spark'):
      ds = load_dataset("llvm-ml/ComPile", split="train[0:1000]")
      #ds = load_dataset("llvm-ml/ComPile", split="train[0:31653]")
    #await asyncio.gather(*(run_subprocess(cmd) for cmd in ds["content"]))
    await asyncio.gather(
      run_subprocess(ds["content"][0]),
run_subprocess(ds["content"][1]),
run_subprocess(ds["content"][2]),
run_subprocess(ds["content"][3]),
run_subprocess(ds["content"][4]),
run_subprocess(ds["content"][5]),
run_subprocess(ds["content"][6]),
run_subprocess(ds["content"][7]),
run_subprocess(ds["content"][8]),
run_subprocess(ds["content"][9]),
run_subprocess(ds["content"][10]),
run_subprocess(ds["content"][11]),
run_subprocess(ds["content"][12]),
run_subprocess(ds["content"][13]),
run_subprocess(ds["content"][14]),
run_subprocess(ds["content"][15]),
run_subprocess(ds["content"][16]),
run_subprocess(ds["content"][17]),
run_subprocess(ds["content"][18]),
run_subprocess(ds["content"][19]),
run_subprocess(ds["content"][20]),
run_subprocess(ds["content"][21]),
run_subprocess(ds["content"][22]),
run_subprocess(ds["content"][23]),
run_subprocess(ds["content"][24]),
run_subprocess(ds["content"][25]),
run_subprocess(ds["content"][26]),
run_subprocess(ds["content"][27]),
run_subprocess(ds["content"][28]),
run_subprocess(ds["content"][29]),
run_subprocess(ds["content"][30]),
run_subprocess(ds["content"][31]),
run_subprocess(ds["content"][32]),
run_subprocess(ds["content"][33]),
run_subprocess(ds["content"][34]),
run_subprocess(ds["content"][35]),
run_subprocess(ds["content"][36]),
run_subprocess(ds["content"][37]),
run_subprocess(ds["content"][38]),
run_subprocess(ds["content"][39]),
run_subprocess(ds["content"][40]),
run_subprocess(ds["content"][41]),
run_subprocess(ds["content"][42]),
run_subprocess(ds["content"][43]),
run_subprocess(ds["content"][44]),
run_subprocess(ds["content"][45]),
run_subprocess(ds["content"][46]),
run_subprocess(ds["content"][47]),
run_subprocess(ds["content"][48]),
run_subprocess(ds["content"][49]),
run_subprocess(ds["content"][50]),
run_subprocess(ds["content"][51]),
run_subprocess(ds["content"][52]),
run_subprocess(ds["content"][53]),
run_subprocess(ds["content"][54]),
run_subprocess(ds["content"][55]),
run_subprocess(ds["content"][56]),
run_subprocess(ds["content"][57]),
run_subprocess(ds["content"][58]),
run_subprocess(ds["content"][59]),
run_subprocess(ds["content"][60]),
run_subprocess(ds["content"][61]),
run_subprocess(ds["content"][62]),
run_subprocess(ds["content"][63]),
run_subprocess(ds["content"][64]),
run_subprocess(ds["content"][65]),
run_subprocess(ds["content"][66]),
run_subprocess(ds["content"][67]),
run_subprocess(ds["content"][68]),
run_subprocess(ds["content"][69]),
run_subprocess(ds["content"][70]),
run_subprocess(ds["content"][71]),
run_subprocess(ds["content"][72]),
run_subprocess(ds["content"][73]),
run_subprocess(ds["content"][74]),
run_subprocess(ds["content"][75]),
run_subprocess(ds["content"][76]),
run_subprocess(ds["content"][77]),
run_subprocess(ds["content"][78]),
run_subprocess(ds["content"][79]),
run_subprocess(ds["content"][80]),
run_subprocess(ds["content"][81]),
run_subprocess(ds["content"][82]),
run_subprocess(ds["content"][83]),
run_subprocess(ds["content"][84]),
run_subprocess(ds["content"][85]),
run_subprocess(ds["content"][86]),
run_subprocess(ds["content"][87]),
run_subprocess(ds["content"][88]),
run_subprocess(ds["content"][89]),
run_subprocess(ds["content"][90]),
run_subprocess(ds["content"][91]),
run_subprocess(ds["content"][92]),
run_subprocess(ds["content"][93]),
run_subprocess(ds["content"][94]),
run_subprocess(ds["content"][95]),
run_subprocess(ds["content"][96]),
run_subprocess(ds["content"][97]),
run_subprocess(ds["content"][98]),
run_subprocess(ds["content"][99]),
run_subprocess(ds["content"][100]),
run_subprocess(ds["content"][101]),
run_subprocess(ds["content"][102]),
run_subprocess(ds["content"][103]),
run_subprocess(ds["content"][104]),
run_subprocess(ds["content"][105]),
run_subprocess(ds["content"][106]),
run_subprocess(ds["content"][107]),
run_subprocess(ds["content"][108]),
run_subprocess(ds["content"][109]),
run_subprocess(ds["content"][110]),
run_subprocess(ds["content"][111]),
run_subprocess(ds["content"][112]),
run_subprocess(ds["content"][113]),
run_subprocess(ds["content"][114]),
run_subprocess(ds["content"][115]),
run_subprocess(ds["content"][116]),
run_subprocess(ds["content"][117]),
run_subprocess(ds["content"][118]),
run_subprocess(ds["content"][119]),
run_subprocess(ds["content"][120]),
run_subprocess(ds["content"][121]),
run_subprocess(ds["content"][122]),
run_subprocess(ds["content"][123]),
run_subprocess(ds["content"][124]),
run_subprocess(ds["content"][125]),
run_subprocess(ds["content"][126]),
run_subprocess(ds["content"][127]),
run_subprocess(ds["content"][128]),
run_subprocess(ds["content"][129]),
run_subprocess(ds["content"][130]),
run_subprocess(ds["content"][131]),
run_subprocess(ds["content"][132]),
run_subprocess(ds["content"][133]),
run_subprocess(ds["content"][134]),
run_subprocess(ds["content"][135]),
run_subprocess(ds["content"][136]),
run_subprocess(ds["content"][137]),
run_subprocess(ds["content"][138]),
run_subprocess(ds["content"][139]),
run_subprocess(ds["content"][140]),
run_subprocess(ds["content"][141]),
run_subprocess(ds["content"][142]),
run_subprocess(ds["content"][143]),
run_subprocess(ds["content"][144]),
run_subprocess(ds["content"][145]),
run_subprocess(ds["content"][146]),
run_subprocess(ds["content"][147]),
run_subprocess(ds["content"][148]),
run_subprocess(ds["content"][149]),
run_subprocess(ds["content"][150]),
run_subprocess(ds["content"][151]),
run_subprocess(ds["content"][152]),
run_subprocess(ds["content"][153]),
run_subprocess(ds["content"][154]),
run_subprocess(ds["content"][155]),
run_subprocess(ds["content"][156]),
run_subprocess(ds["content"][157]),
run_subprocess(ds["content"][158]),
run_subprocess(ds["content"][159]),
run_subprocess(ds["content"][160]),
run_subprocess(ds["content"][161]),
run_subprocess(ds["content"][162]),
run_subprocess(ds["content"][163]),
run_subprocess(ds["content"][164]),
run_subprocess(ds["content"][165]),
run_subprocess(ds["content"][166]),
run_subprocess(ds["content"][167]),
run_subprocess(ds["content"][168]),
run_subprocess(ds["content"][169]),
run_subprocess(ds["content"][170]),
run_subprocess(ds["content"][171]),
run_subprocess(ds["content"][172]),
run_subprocess(ds["content"][173]),
run_subprocess(ds["content"][174]),
run_subprocess(ds["content"][175]),
run_subprocess(ds["content"][176]),
run_subprocess(ds["content"][177]),
run_subprocess(ds["content"][178]),
run_subprocess(ds["content"][179]),
run_subprocess(ds["content"][180]),
run_subprocess(ds["content"][181]),
run_subprocess(ds["content"][182]),
run_subprocess(ds["content"][183]),
run_subprocess(ds["content"][184]),
run_subprocess(ds["content"][185]),
run_subprocess(ds["content"][186]),
run_subprocess(ds["content"][187]),
run_subprocess(ds["content"][188]),
run_subprocess(ds["content"][189]),
run_subprocess(ds["content"][190]),
run_subprocess(ds["content"][191]),
run_subprocess(ds["content"][192]),
run_subprocess(ds["content"][193]),
run_subprocess(ds["content"][194]),
run_subprocess(ds["content"][195]),
run_subprocess(ds["content"][196]),
run_subprocess(ds["content"][197]),
run_subprocess(ds["content"][198]),
run_subprocess(ds["content"][199]),
run_subprocess(ds["content"][200]),
run_subprocess(ds["content"][201]),
run_subprocess(ds["content"][202]),
run_subprocess(ds["content"][203]),
run_subprocess(ds["content"][204]),
run_subprocess(ds["content"][205]),
run_subprocess(ds["content"][206]),
run_subprocess(ds["content"][207]),
run_subprocess(ds["content"][208]),
run_subprocess(ds["content"][209]),
run_subprocess(ds["content"][210]),
run_subprocess(ds["content"][211]),
run_subprocess(ds["content"][212]),
run_subprocess(ds["content"][213]),
run_subprocess(ds["content"][214]),
run_subprocess(ds["content"][215]),
run_subprocess(ds["content"][216]),
run_subprocess(ds["content"][217]),
run_subprocess(ds["content"][218]),
run_subprocess(ds["content"][219]),
run_subprocess(ds["content"][220]),
run_subprocess(ds["content"][221]),
run_subprocess(ds["content"][222]),
run_subprocess(ds["content"][223]),
run_subprocess(ds["content"][224]),
run_subprocess(ds["content"][225]),
run_subprocess(ds["content"][226]),
run_subprocess(ds["content"][227]),
run_subprocess(ds["content"][228]),
run_subprocess(ds["content"][229]),
run_subprocess(ds["content"][230]),
run_subprocess(ds["content"][231]),
run_subprocess(ds["content"][232]),
run_subprocess(ds["content"][233]),
run_subprocess(ds["content"][234]),
run_subprocess(ds["content"][235]),
run_subprocess(ds["content"][236]),
run_subprocess(ds["content"][237]),
run_subprocess(ds["content"][238]),
run_subprocess(ds["content"][239]),
run_subprocess(ds["content"][240]),
run_subprocess(ds["content"][241]),
run_subprocess(ds["content"][242]),
run_subprocess(ds["content"][243]),
run_subprocess(ds["content"][244]),
run_subprocess(ds["content"][245]),
run_subprocess(ds["content"][246]),
run_subprocess(ds["content"][247]),
run_subprocess(ds["content"][248]),
run_subprocess(ds["content"][249]),
run_subprocess(ds["content"][250]),
run_subprocess(ds["content"][251]),
run_subprocess(ds["content"][252]),
run_subprocess(ds["content"][253]),
run_subprocess(ds["content"][254]),
run_subprocess(ds["content"][255]),
run_subprocess(ds["content"][256]),
run_subprocess(ds["content"][257]),
run_subprocess(ds["content"][258]),
run_subprocess(ds["content"][259]),
run_subprocess(ds["content"][260]),
run_subprocess(ds["content"][261]),
run_subprocess(ds["content"][262]),
run_subprocess(ds["content"][263]),
run_subprocess(ds["content"][264]),
run_subprocess(ds["content"][265]),
run_subprocess(ds["content"][266]),
run_subprocess(ds["content"][267]),
run_subprocess(ds["content"][268]),
run_subprocess(ds["content"][269]),
run_subprocess(ds["content"][270]),
run_subprocess(ds["content"][271]),
run_subprocess(ds["content"][272]),
run_subprocess(ds["content"][273]),
run_subprocess(ds["content"][274]),
run_subprocess(ds["content"][275]),
run_subprocess(ds["content"][276]),
run_subprocess(ds["content"][277]),
run_subprocess(ds["content"][278]),
run_subprocess(ds["content"][279]),
run_subprocess(ds["content"][280]),
run_subprocess(ds["content"][281]),
run_subprocess(ds["content"][282]),
run_subprocess(ds["content"][283]),
run_subprocess(ds["content"][284]),
run_subprocess(ds["content"][285]),
run_subprocess(ds["content"][286]),
run_subprocess(ds["content"][287]),
run_subprocess(ds["content"][288]),
run_subprocess(ds["content"][289]),
run_subprocess(ds["content"][290]),
run_subprocess(ds["content"][291]),
run_subprocess(ds["content"][292]),
run_subprocess(ds["content"][293]),
run_subprocess(ds["content"][294]),
run_subprocess(ds["content"][295]),
run_subprocess(ds["content"][296]),
run_subprocess(ds["content"][297]),
run_subprocess(ds["content"][298]),
run_subprocess(ds["content"][299]),
run_subprocess(ds["content"][300]),
run_subprocess(ds["content"][301]),
run_subprocess(ds["content"][302]),
run_subprocess(ds["content"][303]),
run_subprocess(ds["content"][304]),
run_subprocess(ds["content"][305]),
run_subprocess(ds["content"][306]),
run_subprocess(ds["content"][307]),
run_subprocess(ds["content"][308]),
run_subprocess(ds["content"][309]),
run_subprocess(ds["content"][310]),
run_subprocess(ds["content"][311]),
run_subprocess(ds["content"][312]),
run_subprocess(ds["content"][313]),
run_subprocess(ds["content"][314]),
run_subprocess(ds["content"][315]),
run_subprocess(ds["content"][316]),
run_subprocess(ds["content"][317]),
run_subprocess(ds["content"][318]),
run_subprocess(ds["content"][319]),
run_subprocess(ds["content"][320]),
run_subprocess(ds["content"][321]),
run_subprocess(ds["content"][322]),
run_subprocess(ds["content"][323]),
run_subprocess(ds["content"][324]),
run_subprocess(ds["content"][325]),
run_subprocess(ds["content"][326]),
run_subprocess(ds["content"][327]),
run_subprocess(ds["content"][328]),
run_subprocess(ds["content"][329]),
run_subprocess(ds["content"][330]),
run_subprocess(ds["content"][331]),
run_subprocess(ds["content"][332]),
run_subprocess(ds["content"][333]),
run_subprocess(ds["content"][334]),
run_subprocess(ds["content"][335]),
run_subprocess(ds["content"][336]),
run_subprocess(ds["content"][337]),
run_subprocess(ds["content"][338]),
run_subprocess(ds["content"][339]),
run_subprocess(ds["content"][340]),
run_subprocess(ds["content"][341]),
run_subprocess(ds["content"][342]),
run_subprocess(ds["content"][343]),
run_subprocess(ds["content"][344]),
run_subprocess(ds["content"][345]),
run_subprocess(ds["content"][346]),
run_subprocess(ds["content"][347]),
run_subprocess(ds["content"][348]),
run_subprocess(ds["content"][349]),
run_subprocess(ds["content"][350]),
run_subprocess(ds["content"][351]),
run_subprocess(ds["content"][352]),
run_subprocess(ds["content"][353]),
run_subprocess(ds["content"][354]),
run_subprocess(ds["content"][355]),
run_subprocess(ds["content"][356]),
run_subprocess(ds["content"][357]),
run_subprocess(ds["content"][358]),
run_subprocess(ds["content"][359]),
run_subprocess(ds["content"][360]),
run_subprocess(ds["content"][361]),
run_subprocess(ds["content"][362]),
run_subprocess(ds["content"][363]),
run_subprocess(ds["content"][364]),
run_subprocess(ds["content"][365]),
run_subprocess(ds["content"][366]),
run_subprocess(ds["content"][367]),
run_subprocess(ds["content"][368]),
run_subprocess(ds["content"][369]),
run_subprocess(ds["content"][370]),
run_subprocess(ds["content"][371]),
run_subprocess(ds["content"][372]),
run_subprocess(ds["content"][373]),
run_subprocess(ds["content"][374]),
run_subprocess(ds["content"][375]),
run_subprocess(ds["content"][376]),
run_subprocess(ds["content"][377]),
run_subprocess(ds["content"][378]),
run_subprocess(ds["content"][379]),
run_subprocess(ds["content"][380]),
run_subprocess(ds["content"][381]),
run_subprocess(ds["content"][382]),
run_subprocess(ds["content"][383]),
run_subprocess(ds["content"][384]),
run_subprocess(ds["content"][385]),
run_subprocess(ds["content"][386]),
run_subprocess(ds["content"][387]),
run_subprocess(ds["content"][388]),
run_subprocess(ds["content"][389]),
run_subprocess(ds["content"][390]),
run_subprocess(ds["content"][391]),
run_subprocess(ds["content"][392]),
run_subprocess(ds["content"][393]),
run_subprocess(ds["content"][394]),
run_subprocess(ds["content"][395]),
run_subprocess(ds["content"][396]),
run_subprocess(ds["content"][397]),
run_subprocess(ds["content"][398]),
run_subprocess(ds["content"][399]),
run_subprocess(ds["content"][400]),
run_subprocess(ds["content"][401]),
run_subprocess(ds["content"][402]),
run_subprocess(ds["content"][403]),
run_subprocess(ds["content"][404]),
run_subprocess(ds["content"][405]),
run_subprocess(ds["content"][406]),
run_subprocess(ds["content"][407]),
run_subprocess(ds["content"][408]),
run_subprocess(ds["content"][409]),
run_subprocess(ds["content"][410]),
run_subprocess(ds["content"][411]),
run_subprocess(ds["content"][412]),
run_subprocess(ds["content"][413]),
run_subprocess(ds["content"][414]),
run_subprocess(ds["content"][415]),
run_subprocess(ds["content"][416]),
run_subprocess(ds["content"][417]),
run_subprocess(ds["content"][418]),
run_subprocess(ds["content"][419]),
run_subprocess(ds["content"][420]),
run_subprocess(ds["content"][421]),
run_subprocess(ds["content"][422]),
run_subprocess(ds["content"][423]),
run_subprocess(ds["content"][424]),
run_subprocess(ds["content"][425]),
run_subprocess(ds["content"][426]),
run_subprocess(ds["content"][427]),
run_subprocess(ds["content"][428]),
run_subprocess(ds["content"][429]),
run_subprocess(ds["content"][430]),
run_subprocess(ds["content"][431]),
run_subprocess(ds["content"][432]),
run_subprocess(ds["content"][433]),
run_subprocess(ds["content"][434]),
run_subprocess(ds["content"][435]),
run_subprocess(ds["content"][436]),
run_subprocess(ds["content"][437]),
run_subprocess(ds["content"][438]),
run_subprocess(ds["content"][439]),
run_subprocess(ds["content"][440]),
run_subprocess(ds["content"][441]),
run_subprocess(ds["content"][442]),
run_subprocess(ds["content"][443]),
run_subprocess(ds["content"][444]),
run_subprocess(ds["content"][445]),
run_subprocess(ds["content"][446]),
run_subprocess(ds["content"][447]),
run_subprocess(ds["content"][448]),
run_subprocess(ds["content"][449]),
run_subprocess(ds["content"][450]),
run_subprocess(ds["content"][451]),
run_subprocess(ds["content"][452]),
run_subprocess(ds["content"][453]),
run_subprocess(ds["content"][454]),
run_subprocess(ds["content"][455]),
run_subprocess(ds["content"][456]),
run_subprocess(ds["content"][457]),
run_subprocess(ds["content"][458]),
run_subprocess(ds["content"][459]),
run_subprocess(ds["content"][460]),
run_subprocess(ds["content"][461]),
run_subprocess(ds["content"][462]),
run_subprocess(ds["content"][463]),
run_subprocess(ds["content"][464]),
run_subprocess(ds["content"][465]),
run_subprocess(ds["content"][466]),
run_subprocess(ds["content"][467]),
run_subprocess(ds["content"][468]),
run_subprocess(ds["content"][469]),
run_subprocess(ds["content"][470]),
run_subprocess(ds["content"][471]),
run_subprocess(ds["content"][472]),
run_subprocess(ds["content"][473]),
run_subprocess(ds["content"][474]),
run_subprocess(ds["content"][475]),
run_subprocess(ds["content"][476]),
run_subprocess(ds["content"][477]),
run_subprocess(ds["content"][478]),
run_subprocess(ds["content"][479]),
run_subprocess(ds["content"][480]),
run_subprocess(ds["content"][481]),
run_subprocess(ds["content"][482]),
run_subprocess(ds["content"][483]),
run_subprocess(ds["content"][484]),
run_subprocess(ds["content"][485]),
run_subprocess(ds["content"][486]),
run_subprocess(ds["content"][487]),
run_subprocess(ds["content"][488]),
run_subprocess(ds["content"][489]),
run_subprocess(ds["content"][490]),
run_subprocess(ds["content"][491]),
run_subprocess(ds["content"][492]),
run_subprocess(ds["content"][493]),
run_subprocess(ds["content"][494]),
run_subprocess(ds["content"][495]),
run_subprocess(ds["content"][496]),
run_subprocess(ds["content"][497]),
run_subprocess(ds["content"][498]),
run_subprocess(ds["content"][499]),
run_subprocess(ds["content"][500]),
run_subprocess(ds["content"][501]),
run_subprocess(ds["content"][502]),
run_subprocess(ds["content"][503]),
run_subprocess(ds["content"][504]),
run_subprocess(ds["content"][505]),
run_subprocess(ds["content"][506]),
run_subprocess(ds["content"][507]),
run_subprocess(ds["content"][508]),
run_subprocess(ds["content"][509]),
run_subprocess(ds["content"][510]),
run_subprocess(ds["content"][511]),
run_subprocess(ds["content"][512]),
run_subprocess(ds["content"][513]),
run_subprocess(ds["content"][514]),
run_subprocess(ds["content"][515]),
run_subprocess(ds["content"][516]),
run_subprocess(ds["content"][517]),
run_subprocess(ds["content"][518]),
run_subprocess(ds["content"][519]),
run_subprocess(ds["content"][520]),
run_subprocess(ds["content"][521]),
run_subprocess(ds["content"][522]),
run_subprocess(ds["content"][523]),
run_subprocess(ds["content"][524]),
run_subprocess(ds["content"][525]),
run_subprocess(ds["content"][526]),
run_subprocess(ds["content"][527]),
run_subprocess(ds["content"][528]),
run_subprocess(ds["content"][529]),
run_subprocess(ds["content"][530]),
run_subprocess(ds["content"][531]),
run_subprocess(ds["content"][532]),
run_subprocess(ds["content"][533]),
run_subprocess(ds["content"][534]),
run_subprocess(ds["content"][535]),
run_subprocess(ds["content"][536]),
run_subprocess(ds["content"][537]),
run_subprocess(ds["content"][538]),
run_subprocess(ds["content"][539]),
run_subprocess(ds["content"][540]),
run_subprocess(ds["content"][541]),
run_subprocess(ds["content"][542]),
run_subprocess(ds["content"][543]),
run_subprocess(ds["content"][544]),
run_subprocess(ds["content"][545]),
run_subprocess(ds["content"][546]),
run_subprocess(ds["content"][547]),
run_subprocess(ds["content"][548]),
run_subprocess(ds["content"][549]),
run_subprocess(ds["content"][550]),
run_subprocess(ds["content"][551]),
run_subprocess(ds["content"][552]),
run_subprocess(ds["content"][553]),
run_subprocess(ds["content"][554]),
run_subprocess(ds["content"][555]),
run_subprocess(ds["content"][556]),
run_subprocess(ds["content"][557]),
run_subprocess(ds["content"][558]),
run_subprocess(ds["content"][559]),
run_subprocess(ds["content"][560]),
run_subprocess(ds["content"][561]),
run_subprocess(ds["content"][562]),
run_subprocess(ds["content"][563]),
run_subprocess(ds["content"][564]),
run_subprocess(ds["content"][565]),
run_subprocess(ds["content"][566]),
run_subprocess(ds["content"][567]),
run_subprocess(ds["content"][568]),
run_subprocess(ds["content"][569]),
run_subprocess(ds["content"][570]),
run_subprocess(ds["content"][571]),
run_subprocess(ds["content"][572]),
run_subprocess(ds["content"][573]),
run_subprocess(ds["content"][574]),
run_subprocess(ds["content"][575]),
run_subprocess(ds["content"][576]),
run_subprocess(ds["content"][577]),
run_subprocess(ds["content"][578]),
run_subprocess(ds["content"][579]),
run_subprocess(ds["content"][580]),
run_subprocess(ds["content"][581]),
run_subprocess(ds["content"][582]),
run_subprocess(ds["content"][583]),
run_subprocess(ds["content"][584]),
run_subprocess(ds["content"][585]),
run_subprocess(ds["content"][586]),
run_subprocess(ds["content"][587]),
run_subprocess(ds["content"][588]),
run_subprocess(ds["content"][589]),
run_subprocess(ds["content"][590]),
run_subprocess(ds["content"][591]),
run_subprocess(ds["content"][592]),
run_subprocess(ds["content"][593]),
run_subprocess(ds["content"][594]),
run_subprocess(ds["content"][595]),
run_subprocess(ds["content"][596]),
run_subprocess(ds["content"][597]),
run_subprocess(ds["content"][598]),
run_subprocess(ds["content"][599]),
run_subprocess(ds["content"][600]),
run_subprocess(ds["content"][601]),
run_subprocess(ds["content"][602]),
run_subprocess(ds["content"][603]),
run_subprocess(ds["content"][604]),
run_subprocess(ds["content"][605]),
run_subprocess(ds["content"][606]),
run_subprocess(ds["content"][607]),
run_subprocess(ds["content"][608]),
run_subprocess(ds["content"][609]),
run_subprocess(ds["content"][610]),
run_subprocess(ds["content"][611]),
run_subprocess(ds["content"][612]),
run_subprocess(ds["content"][613]),
run_subprocess(ds["content"][614]),
run_subprocess(ds["content"][615]),
run_subprocess(ds["content"][616]),
run_subprocess(ds["content"][617]),
run_subprocess(ds["content"][618]),
run_subprocess(ds["content"][619]),
run_subprocess(ds["content"][620]),
run_subprocess(ds["content"][621]),
run_subprocess(ds["content"][622]),
run_subprocess(ds["content"][623]),
run_subprocess(ds["content"][624]),
run_subprocess(ds["content"][625]),
run_subprocess(ds["content"][626]),
run_subprocess(ds["content"][627]),
run_subprocess(ds["content"][628]),
run_subprocess(ds["content"][629]),
run_subprocess(ds["content"][630]),
run_subprocess(ds["content"][631]),
run_subprocess(ds["content"][632]),
run_subprocess(ds["content"][633]),
run_subprocess(ds["content"][634]),
run_subprocess(ds["content"][635]),
run_subprocess(ds["content"][636]),
run_subprocess(ds["content"][637]),
run_subprocess(ds["content"][638]),
run_subprocess(ds["content"][639]),
run_subprocess(ds["content"][640]),
run_subprocess(ds["content"][641]),
run_subprocess(ds["content"][642]),
run_subprocess(ds["content"][643]),
run_subprocess(ds["content"][644]),
run_subprocess(ds["content"][645]),
run_subprocess(ds["content"][646]),
run_subprocess(ds["content"][647]),
run_subprocess(ds["content"][648]),
run_subprocess(ds["content"][649]),
run_subprocess(ds["content"][650]),
run_subprocess(ds["content"][651]),
run_subprocess(ds["content"][652]),
run_subprocess(ds["content"][653]),
run_subprocess(ds["content"][654]),
run_subprocess(ds["content"][655]),
run_subprocess(ds["content"][656]),
run_subprocess(ds["content"][657]),
run_subprocess(ds["content"][658]),
run_subprocess(ds["content"][659]),
run_subprocess(ds["content"][660]),
run_subprocess(ds["content"][661]),
run_subprocess(ds["content"][662]),
run_subprocess(ds["content"][663]),
run_subprocess(ds["content"][664]),
run_subprocess(ds["content"][665]),
run_subprocess(ds["content"][666]),
run_subprocess(ds["content"][667]),
run_subprocess(ds["content"][668]),
run_subprocess(ds["content"][669]),
run_subprocess(ds["content"][670]),
run_subprocess(ds["content"][671]),
run_subprocess(ds["content"][672]),
run_subprocess(ds["content"][673]),
run_subprocess(ds["content"][674]),
run_subprocess(ds["content"][675]),
run_subprocess(ds["content"][676]),
run_subprocess(ds["content"][677]),
run_subprocess(ds["content"][678]),
run_subprocess(ds["content"][679]),
run_subprocess(ds["content"][680]),
run_subprocess(ds["content"][681]),
run_subprocess(ds["content"][682]),
run_subprocess(ds["content"][683]),
run_subprocess(ds["content"][684]),
run_subprocess(ds["content"][685]),
run_subprocess(ds["content"][686]),
run_subprocess(ds["content"][687]),
run_subprocess(ds["content"][688]),
run_subprocess(ds["content"][689]),
run_subprocess(ds["content"][690]),
run_subprocess(ds["content"][691]),
run_subprocess(ds["content"][692]),
run_subprocess(ds["content"][693]),
run_subprocess(ds["content"][694]),
run_subprocess(ds["content"][695]),
run_subprocess(ds["content"][696]),
run_subprocess(ds["content"][697]),
run_subprocess(ds["content"][698]),
run_subprocess(ds["content"][699]),
run_subprocess(ds["content"][700]),
run_subprocess(ds["content"][701]),
run_subprocess(ds["content"][702]),
run_subprocess(ds["content"][703]),
run_subprocess(ds["content"][704]),
run_subprocess(ds["content"][705]),
run_subprocess(ds["content"][706]),
run_subprocess(ds["content"][707]),
run_subprocess(ds["content"][708]),
run_subprocess(ds["content"][709]),
run_subprocess(ds["content"][710]),
run_subprocess(ds["content"][711]),
run_subprocess(ds["content"][712]),
run_subprocess(ds["content"][713]),
run_subprocess(ds["content"][714]),
run_subprocess(ds["content"][715]),
run_subprocess(ds["content"][716]),
run_subprocess(ds["content"][717]),
run_subprocess(ds["content"][718]),
run_subprocess(ds["content"][719]),
run_subprocess(ds["content"][720]),
run_subprocess(ds["content"][721]),
run_subprocess(ds["content"][722]),
run_subprocess(ds["content"][723]),
run_subprocess(ds["content"][724]),
run_subprocess(ds["content"][725]),
run_subprocess(ds["content"][726]),
run_subprocess(ds["content"][727]),
run_subprocess(ds["content"][728]),
run_subprocess(ds["content"][729]),
run_subprocess(ds["content"][730]),
run_subprocess(ds["content"][731]),
run_subprocess(ds["content"][732]),
run_subprocess(ds["content"][733]),
run_subprocess(ds["content"][734]),
run_subprocess(ds["content"][735]),
run_subprocess(ds["content"][736]),
run_subprocess(ds["content"][737]),
run_subprocess(ds["content"][738]),
run_subprocess(ds["content"][739]),
run_subprocess(ds["content"][740]),
run_subprocess(ds["content"][741]),
run_subprocess(ds["content"][742]),
run_subprocess(ds["content"][743]),
run_subprocess(ds["content"][744]),
run_subprocess(ds["content"][745]),
run_subprocess(ds["content"][746]),
run_subprocess(ds["content"][747]),
run_subprocess(ds["content"][748]),
run_subprocess(ds["content"][749]),
run_subprocess(ds["content"][750]),
run_subprocess(ds["content"][751]),
run_subprocess(ds["content"][752]),
run_subprocess(ds["content"][753]),
run_subprocess(ds["content"][754]),
run_subprocess(ds["content"][755]),
run_subprocess(ds["content"][756]),
run_subprocess(ds["content"][757]),
run_subprocess(ds["content"][758]),
run_subprocess(ds["content"][759]),
run_subprocess(ds["content"][760]),
run_subprocess(ds["content"][761]),
run_subprocess(ds["content"][762]),
run_subprocess(ds["content"][763]),
run_subprocess(ds["content"][764]),
run_subprocess(ds["content"][765]),
run_subprocess(ds["content"][766]),
run_subprocess(ds["content"][767]),
run_subprocess(ds["content"][768]),
run_subprocess(ds["content"][769]),
run_subprocess(ds["content"][770]),
run_subprocess(ds["content"][771]),
run_subprocess(ds["content"][772]),
run_subprocess(ds["content"][773]),
run_subprocess(ds["content"][774]),
run_subprocess(ds["content"][775]),
run_subprocess(ds["content"][776]),
run_subprocess(ds["content"][777]),
run_subprocess(ds["content"][778]),
run_subprocess(ds["content"][779]),
run_subprocess(ds["content"][780]),
run_subprocess(ds["content"][781]),
run_subprocess(ds["content"][782]),
run_subprocess(ds["content"][783]),
run_subprocess(ds["content"][784]),
run_subprocess(ds["content"][785]),
run_subprocess(ds["content"][786]),
run_subprocess(ds["content"][787]),
run_subprocess(ds["content"][788]),
run_subprocess(ds["content"][789]),
run_subprocess(ds["content"][790]),
run_subprocess(ds["content"][791]),
run_subprocess(ds["content"][792]),
run_subprocess(ds["content"][793]),
run_subprocess(ds["content"][794]),
run_subprocess(ds["content"][795]),
run_subprocess(ds["content"][796]),
run_subprocess(ds["content"][797]),
run_subprocess(ds["content"][798]),
run_subprocess(ds["content"][799]),
run_subprocess(ds["content"][800]),
run_subprocess(ds["content"][801]),
run_subprocess(ds["content"][802]),
run_subprocess(ds["content"][803]),
run_subprocess(ds["content"][804]),
run_subprocess(ds["content"][805]),
run_subprocess(ds["content"][806]),
run_subprocess(ds["content"][807]),
run_subprocess(ds["content"][808]),
run_subprocess(ds["content"][809]),
run_subprocess(ds["content"][810]),
run_subprocess(ds["content"][811]),
run_subprocess(ds["content"][812]),
run_subprocess(ds["content"][813]),
run_subprocess(ds["content"][814]),
run_subprocess(ds["content"][815]),
run_subprocess(ds["content"][816]),
run_subprocess(ds["content"][817]),
run_subprocess(ds["content"][818]),
run_subprocess(ds["content"][819]),
run_subprocess(ds["content"][820]),
run_subprocess(ds["content"][821]),
run_subprocess(ds["content"][822]),
run_subprocess(ds["content"][823]),
run_subprocess(ds["content"][824]),
run_subprocess(ds["content"][825]),
run_subprocess(ds["content"][826]),
run_subprocess(ds["content"][827]),
run_subprocess(ds["content"][828]),
run_subprocess(ds["content"][829]),
run_subprocess(ds["content"][830]),
run_subprocess(ds["content"][831]),
run_subprocess(ds["content"][832]),
run_subprocess(ds["content"][833]),
run_subprocess(ds["content"][834]),
run_subprocess(ds["content"][835]),
run_subprocess(ds["content"][836]),
run_subprocess(ds["content"][837]),
run_subprocess(ds["content"][838]),
run_subprocess(ds["content"][839]),
run_subprocess(ds["content"][840]),
run_subprocess(ds["content"][841]),
run_subprocess(ds["content"][842]),
run_subprocess(ds["content"][843]),
run_subprocess(ds["content"][844]),
run_subprocess(ds["content"][845]),
run_subprocess(ds["content"][846]),
run_subprocess(ds["content"][847]),
run_subprocess(ds["content"][848]),
run_subprocess(ds["content"][849]),
run_subprocess(ds["content"][850]),
run_subprocess(ds["content"][851]),
run_subprocess(ds["content"][852]),
run_subprocess(ds["content"][853]),
run_subprocess(ds["content"][854]),
run_subprocess(ds["content"][855]),
run_subprocess(ds["content"][856]),
run_subprocess(ds["content"][857]),
run_subprocess(ds["content"][858]),
run_subprocess(ds["content"][859]),
run_subprocess(ds["content"][860]),
run_subprocess(ds["content"][861]),
run_subprocess(ds["content"][862]),
run_subprocess(ds["content"][863]),
run_subprocess(ds["content"][864]),
run_subprocess(ds["content"][865]),
run_subprocess(ds["content"][866]),
run_subprocess(ds["content"][867]),
run_subprocess(ds["content"][868]),
run_subprocess(ds["content"][869]),
run_subprocess(ds["content"][870]),
run_subprocess(ds["content"][871]),
run_subprocess(ds["content"][872]),
run_subprocess(ds["content"][873]),
run_subprocess(ds["content"][874]),
run_subprocess(ds["content"][875]),
run_subprocess(ds["content"][876]),
run_subprocess(ds["content"][877]),
run_subprocess(ds["content"][878]),
run_subprocess(ds["content"][879]),
run_subprocess(ds["content"][880]),
run_subprocess(ds["content"][881]),
run_subprocess(ds["content"][882]),
run_subprocess(ds["content"][883]),
run_subprocess(ds["content"][884]),
run_subprocess(ds["content"][885]),
run_subprocess(ds["content"][886]),
run_subprocess(ds["content"][887]),
run_subprocess(ds["content"][888]),
run_subprocess(ds["content"][889]),
run_subprocess(ds["content"][890]),
run_subprocess(ds["content"][891]),
run_subprocess(ds["content"][892]),
run_subprocess(ds["content"][893]),
run_subprocess(ds["content"][894]),
run_subprocess(ds["content"][895]),
run_subprocess(ds["content"][896]),
run_subprocess(ds["content"][897]),
run_subprocess(ds["content"][898]),
run_subprocess(ds["content"][899]),
run_subprocess(ds["content"][900]),
run_subprocess(ds["content"][901]),
run_subprocess(ds["content"][902]),
run_subprocess(ds["content"][903]),
run_subprocess(ds["content"][904]),
run_subprocess(ds["content"][905]),
run_subprocess(ds["content"][906]),
run_subprocess(ds["content"][907]),
run_subprocess(ds["content"][908]),
run_subprocess(ds["content"][909]),
run_subprocess(ds["content"][910]),
run_subprocess(ds["content"][911]),
run_subprocess(ds["content"][912]),
run_subprocess(ds["content"][913]),
run_subprocess(ds["content"][914]),
run_subprocess(ds["content"][915]),
run_subprocess(ds["content"][916]),
run_subprocess(ds["content"][917]),
run_subprocess(ds["content"][918]),
run_subprocess(ds["content"][919]),
run_subprocess(ds["content"][920]),
run_subprocess(ds["content"][921]),
run_subprocess(ds["content"][922]),
run_subprocess(ds["content"][923]),
run_subprocess(ds["content"][924]),
run_subprocess(ds["content"][925]),
run_subprocess(ds["content"][926]),
run_subprocess(ds["content"][927]),
run_subprocess(ds["content"][928]),
run_subprocess(ds["content"][929]),
run_subprocess(ds["content"][930]),
run_subprocess(ds["content"][931]),
run_subprocess(ds["content"][932]),
run_subprocess(ds["content"][933]),
run_subprocess(ds["content"][934]),
run_subprocess(ds["content"][935]),
run_subprocess(ds["content"][936]),
run_subprocess(ds["content"][937]),
run_subprocess(ds["content"][938]),
run_subprocess(ds["content"][939]),
run_subprocess(ds["content"][940]),
run_subprocess(ds["content"][941]),
run_subprocess(ds["content"][942]),
run_subprocess(ds["content"][943]),
run_subprocess(ds["content"][944]),
run_subprocess(ds["content"][945]),
run_subprocess(ds["content"][946]),
run_subprocess(ds["content"][947]),
run_subprocess(ds["content"][948]),
run_subprocess(ds["content"][949]),
run_subprocess(ds["content"][950]),
run_subprocess(ds["content"][951]),
run_subprocess(ds["content"][952]),
run_subprocess(ds["content"][953]),
run_subprocess(ds["content"][954]),
run_subprocess(ds["content"][955]),
run_subprocess(ds["content"][956]),
run_subprocess(ds["content"][957]),
run_subprocess(ds["content"][958]),
run_subprocess(ds["content"][959]),
run_subprocess(ds["content"][960]),
run_subprocess(ds["content"][961]),
run_subprocess(ds["content"][962]),
run_subprocess(ds["content"][963]),
run_subprocess(ds["content"][964]),
run_subprocess(ds["content"][965]),
run_subprocess(ds["content"][966]),
run_subprocess(ds["content"][967]),
run_subprocess(ds["content"][968]),
run_subprocess(ds["content"][969]),
run_subprocess(ds["content"][970]),
run_subprocess(ds["content"][971]),
run_subprocess(ds["content"][972]),
run_subprocess(ds["content"][973]),
run_subprocess(ds["content"][974]),
run_subprocess(ds["content"][975]),
run_subprocess(ds["content"][976]),
run_subprocess(ds["content"][977]),
run_subprocess(ds["content"][978]),
run_subprocess(ds["content"][979]),
run_subprocess(ds["content"][980]),
run_subprocess(ds["content"][981]),
run_subprocess(ds["content"][982]),
run_subprocess(ds["content"][983]),
run_subprocess(ds["content"][984]),
run_subprocess(ds["content"][985]),
run_subprocess(ds["content"][986]),
run_subprocess(ds["content"][987]),
run_subprocess(ds["content"][988]),
run_subprocess(ds["content"][989]),
run_subprocess(ds["content"][990]),
run_subprocess(ds["content"][991]),
run_subprocess(ds["content"][992]),
run_subprocess(ds["content"][993]),
run_subprocess(ds["content"][994]),
run_subprocess(ds["content"][995]),
run_subprocess(ds["content"][996]),
run_subprocess(ds["content"][997]),
run_subprocess(ds["content"][998]),
run_subprocess(ds["content"][999])
    )

asyncio.run(main())
