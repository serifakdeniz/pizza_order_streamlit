import streamlit as st
import sqlite3

conn=sqlite3.connect("pizzadb.sqlite3")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS siparisler(isim TEXT,adres TEXT,pizza TEXT,boy TEXT,icecek TEXT,fiyat REAL)")
conn.commit()
c.execute("select isim from pizzalar")

isimler=c.fetchall()

isimlerlist=[]
for i in isimler:
    isimlerlist.append(i[0])





st.header("Siparis")



with st.form("siparis",clear_on_submit=True):
    isim=st.text_input("isim soyisim")
    pizza=st.selectbox("pizza sec",isimlerlist)
    boy=st.selectbox("boy",["small","medium","large"])
    icecek=st.selectbox("icecek",["Ayran","Soda","Ice tea"])
    adres=st.text_area("adres")
    siparisver=st.form_submit_button("siparişver")


    if siparisver:
        if boy=="small":
            c.execute("SELECT smfiyat FROM pizzalar where isim=?",(pizza,))
            fiyat=c.fetchone()
        elif boy=="medium":
            c.execute("SELECT mdfiyat FROM pizzalar where isim=?",(pizza,))
            fiyat=c.fetchone()
        elif boy=="large":
            c.execute("SELECT lgfiyat FROM pizzalar where isim=?",(pizza,))
            fiyat=c.fetchone()

    

        icecekler={
            "Ayran":45,
            "Soda":50,
            "Ice tea":70
        } 

        icecekfiyat=icecekler[icecek]
        toplamfiyat=fiyat[0]+icecekfiyat
        st.write(toplamfiyat)


        c.execute("INSERT INTO siparisler VALUES(?,?,?,?,?,?)",(isim,adres,pizza,boy,icecek,toplamfiyat))
        conn.commit()
        st.success(f"sipariş başarılı şekilde gerçeekleşti  toplam fiyat{toplamfiyat} lira")