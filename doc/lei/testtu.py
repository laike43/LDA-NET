from sqlconnect import Sqldata
import community
import networkx as nx
import matplotlib.pyplot as plt
#定义有向图
import datetime
from dateutil.relativedelta import relativedelta

def timeadd(linitdate,month):
    #linitdate = "2017-07-18"
    date_time = datetime.datetime.strptime(linitdate, '%Y-%m-%d')
    now = date_time - relativedelta(months=-month)
    return now.strftime('%Y%m%d')
initdate = '2001-1-1'

x={'-persson@ricemail.ricefinancial.com': 0, '01019@salespoint.dealerconnection.com': 0, '0_19812_e719a090-7eca-d011-9d39-0000f84121eb_us@newsletters.microsoft.com': 2, '1.10969419.-2@multexinvestornetwork.com': 0, '1.11176403.-2@multexinvestornetwork.com': 0, '1.12714936.-2@multexinvestornetwork.com': 0, '1.11307318.-3@multexinvestornetwork.com': 0, '1.3243.ad-ld1a17bbsold.1@mailer.realage.com': 0, '1.3262.cb-rhfp1yfr-7gf.1@mailer.realage.com': 4, '10182829@mbox.surecom.com': 0, '1.3993.cd-yjit17fk3xoa.1@mailer.realage.com': 4, '101qi@msn.com': 0, '10d3z37pga8@msn.com': 0, '10jribnick@interchange-energy.com': 0, '11-jribnick@interchange-energy.com': 5, '15126-1029@m2.innovyx.com': 10, '15126-994@m2.innovyx.com': 1, '1800flowers.217260508@s2u2.com': 0, '1800flowers.224433405@s2u2.com': 0, '1800flowers.23274514@s2u2.com': 1, '1800flowers.235677224@s2u2.com': 0, '1800flowers.237779281@s2u2.com': 0, '1800flowers.243967005@s2u2.com': 0, '1800flowers.237779293@s2u2.com': 0, '1800flowers.96663423@s2u2.com': 10, '1800flowers@1800flowers.flonetwork.com': 0, '1a7info1@altavista.se': 0, '1a7info@polisen.nu': 0, '2.2873.48-oy0-gd2ovdf6.1@cda01.cdnow.com': 0, '2.2873.72-cxtvsrmukelc.1@cda01.cdnow.com': 0, '2.3758.c8-1utp_qhzzgrr.1@ummail1.unitedmedia.com': 9, '26101652@yahoo.com': 0, '2kylb8@msn.com': 0, '403097.167547968.1@news.forbesdigital.com': 4, '403098.167547968.1@news.forbesdigital.com': 0, '405953.124936407.2@1.americanexpress.com': 0, '403159.221472852.3@newsbyemail.ft.com': 0, '407982.126941280.2@1.americanexpress.com': 1, '40ees@enron.com': 0, '40enron@enron.com': 0, '419525.167547968.1@news.forbesdigital.com': 1, '419899.247679897.1@newsbyemail.ft.com': 0, '42.6859.55-takaoksqcozrdr4xmdrr.1@e-mailprograms.delta.com': 0, '42.6991.e9-gdmp_xx0ornue8m9q9rr.1@e-mailprograms.delta.com': 5, '42.9102.e9-gdmp_x60odnme1mvcdrr.1@e-mailprograms.delta.com': 0, '424366.167547968.1@news.forbesdigital.com': 0, '434481.282903899.1@newsbyemail.ft.com': 0, '448753.26815304.1@1.americanexpress.com': 1, '448753.126941280.1@1.americanexpress.com': 0, '462260.86351074.2@1.americanexpress.com': 0, '478124.86351074.2@1.americanexpress.com': 0, '548@britishparts.com': 0, '5moore@family.net': 3, '6.996.df-_z3y_13lxjmfprrr.1@mail3.travelocity.com': 2, '6.971.f4-bmy016csspwv.1@mail3.travelocity.com': 1, '6.ews@enron.com': 0, '7409949@skytel.com': 1, '7409950@skytel.com': 0, '8772374503@pagenetmessage.net': 0, '8772376735@pagenetmessage.net': 3, '8774754543@skytel.com': 0, '8777865122@skytel.com': 0, '8888915473@archwireless.net': 0, '8778044255@skytel.com': 0, '888annotated@potomac.com': 2, '8dznl4fzr@msn.com': 0, '9069761@skytel.com': 0, '9069876@skytel.com': 0, 'a..davis@enron.com': 10, 'a..garcia@enron.com': 0, 'a..gomez@enron.com': 0, 'a..hope@enron.com': 0, 'a..howard@enron.com': 9, 'a..hueter@enron.com': 3, 'a..hughes@enron.com': 0, 'a..lee@enron.com': 0, 'a..knudsen@enron.com': 0, 'a..lindholm@enron.com': 0, 'a..roberts@enron.com': 0, 'a..robison@enron.com': 2, 'a..schroeder@enron.com': 11, 'a..smith@enron.com': 5, 'a.taylor@enron.com': 5, 'a3e5t4s7w3t@hotmail.com': 0, 'aairmail@info.aa.com': 5, 'aarbisser@kayescholer.com': 5, 'aamir.maniar@enron.com': 5, 'aamarks@apmrecruiting.com': 4, 'aaron.armstrong@enron.com': 0, 'aaron.berutti@enron.com': 5, 'aaron.brown@enron.com': 9, 'aaron.klemm@enron.com': 5, 'aaron.martinsen@enron.com': 5, 'aaron.thomas@aesmail.com': 0, 'aaron@global2000.net': 0, 'aavalos@pnm.com': 0, 'abaker@skippingstone.com': 10, 'abaxter@houston.rr.com': 10, 'abb@eslawfirm.com': 5, 'abcnewsnow-editor@mail.abcnews.go.com': 9, 'abc111@mail.uole.com.ve': 0, 'abel@enron.com': 4, 'abillings@knowledgeinenergy.com': 6, 'abmcdon@yahoo.com': 6, 'abourne@alec.org': 6, 'aborn886@yahoo.com': 6, 'about-shoppingextra@aboutdirect.net': 7, 'abraham5@flash.net': 9, 'abrock@poloralphlauren.com': 0, 'aburman@earthlink.net': 0, 'ac1111@earthlink.net': 1, 'absolute_best@superemailservice.com': 6, 'acahanchian@zdnetonebox.com': 0, 'account-update@amazon.com': 0, 'accountit@autorelister.com': 2, 'accountmanager@shockwave.com': 6, 'accountinformation@community.nextcard.com': 3, 'accounts@ezboard.com': 2, 'accthelp@cooltravelassistant.com': 0, 'accthelp@support.expedia.com': 2, 'acedirect@aircanada.ca': 6, 'ach247@netscape.net': 1, 'achokshi@firstcallassociates.com': 2, 'achowdhr@uschamber.com': 9, 'acinfo@aircanada.ca': 9, 'ack@aelaw.com': 1, 'ackertdm@yahoo.com': 1, 'ackc@msn.com': 0, 'aclair@moheck.com': 0, 'aclark@firstcallassociates.com': 0, 'acormier@vicr.com': 1, 'acullen@firstcallassociates.com': 4, 'acunningham@technologicp.com': 6, 'acurry@velaw.com': 4, 'ada@kochgallery.com': 4, 'adam.bayer@enron.com': 2, 'adam.giannone@enron.com': 11, 'adam.johnson@enron.com': 0, 'adam.overfield@enron.com': 0, 'adam.siegel@enron.com': 10, 'adam.umanoff@enron.com': 1, 'adamk@nepco.com': 0, 'adamsholly@netscape.net': 4, 'adanker@kayescholer.com': 2, 'adarsh.vakharia@enron.com': 4, 'adefelice@ggfcmk.com': 10, 'adel.robinson@enron.com': 6, 'adeleon@lionforce.com': 0, 'adentiii@houston.rr.com': 4, 'adesell@nyiso.com': 4, 'admcgown@ev1.net': 11, 'adesioye@u-t-g.de': 11, 'adityad@wharton.upenn.edu': 11, 'admin.enron@enron.com': 0, 'administration.enron@enron.com': 0, 'adminsec@centralhouston.org': 6, 'administrator@wyden.senate.gov': 1, 'adnan.patel@enron.com': 6, 'adonnell@prmllp.com': 7, 'adolfo_montesinos@mckinsey.com': 8, 'adrial.boals@enron.com': 0, 'adriana.wynn@enron.com': 6, 'adriane.schultea@enron.com': 6, 'adrianne.engler@enron.com': 1, 'adsmith@brobeck.com': 6, 'aduncan@kilstock.com': 8, 'advadv@ruraltel.net': 0, 'advdfeedback@investools.com': 6, 'aepin@aep.com': 8, 'aerozonajet@qwest.net': 8, 'af@tozzini.com.br': 9, 'afinch@iasco.com': 4, 'afpaschke@bpa.gov': 7, 'aftab.saleem@enron.com': 0, 'afternoon29@alerts.equityalert.com': 0, 'agallers@yahoo.com': 0, 'agapefndg@enron.com': 0, 'agatha.tran@enron.com': 8, 'agbriggs@adamswells.com': 8, 'agold@coral-energy.com': 1, 'agovenar@govadv.com': 2, 'agrasso@exchange.ml.com': 7, 'agustin.perez@enron.com': 7, 'aguilera-peon@enron.com': 0, 'ahadonation@heart.org': 1, 'ahafner2@csc.com': 1, 'ahebert@akingump.com': 7, 'aheinle@midwestiso.org': 7, 'aherbst@utilisenergy.com': 7, 'aherrera@statoilenergy.com': 4, 'aiazkazi@hotbot.com': 0, 'ahockman2@attbroadband.com': 0, 'aiaz_kazi@versata.com': 4, 'aimee.lannou@enron.com': 0, 'aimr2001@bbh1.viamedialinq.com': 0, 'aimspecialoffers@offers.aol.com': 11, 'airam.arteaga@enron.com': 0, 'airtran_airways_net_escapes.um.a.35.127@post.intellimedia.com': 0, 'airtran_airways_net_escapes@post.intellimedia.com': 2, 'aishikawa@socalgas.com': 4, 'ajones@uwtgc.org': 0, 'akatz@eei.org': 0, 'akhan@khanventures.com': 0, 'akoelemay@cogc.com': 0, 'akretz@glasgowmedicalcenter.com': 0, 'al@friedwire.com': 0, 'alaadin.suliman@enron.com': 0, 'aladdin@customoffers.com': 0, 'alafave@houston.org': 0, 'alamonsoff@watersinfo.com': 0, 'alan.aronowitz@enron.com': 0, 'alan.bransgrove@xemkt.com': 9, 'alan.comnes@enron.com': 0, 'alan.larsen@enron.com': 0, 'alan.engberg@enron.com': 0, 'alan.wright@us.cibc.com': 0, 'alan@enventure.com': 5, 'alb@cpuc.ca.gov': 0, 'albert.escamilla@enron.com': 1, 'albert.meyers@enron.com': 0, 'alberto.levy@enron.com': 0, 'alberto.gude@enron.com': 9, 'alder@enron.com': 0, 'alberto_jaramillo@putnaminv.com': 0, 'alden.alleman@elpaso.com': 0, 'alec.cohen@creditlyonnais.co.uk': 0, 'aleck.dadson@enron.com': 0, 'aleck.dadson@ngwi.com': 0, 'alejandra.chavez@enron.com': 0, 'aleonard@caiso.com': 0, 'alert@venturewire.com': 0, 'alerts-breakingnews@yahoo-inc.com': 0, 'alerts-finance@yahoo-inc.com': 3, 'alerts@alerts.equityalert.com': 0}



def grape(x):

    DG = nx.Graph()

    for key,values in  x.items():
        DG.add_node(key)
        for name, idclass in x.items():
            DG.add_node(name)
            if values == idclass:
                DG.add_edge(key,name)

    # colors = ['red', 'green', 'blue', 'yellow']
    nx.draw(DG, with_labels=False, node_size=8)
    plt.show()
    G = DG
    partition = community.best_partition(G)

    # drawing
    size = float(len(set(partition.values())))
    pos = nx.spring_layout(G)
    count = 0.
    for com in set(partition.values()):
        count = count + 1.
        list_nodes = [nodes for nodes in partition.keys()
                      if partition[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20,
                               node_color=str(count / size))

    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()
grape(x)
#colors = ['red', 'green', 'blue', 'yellow']

'''
partition = community.best_partition(G)

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


nx.draw_networkx_edges(G,pos, alpha=0.5)
plt.show()
'''