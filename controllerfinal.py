#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('base12.db')
    con.row_factory = sqlite3.Row
    return con


def get_ingredientes():
    con = connect()
    c = con.cursor()
    query = """SELECT recetas.ingredientes FROM recetas,categorias where recetas.fk_id_categoria=categorias.id_categoria"""
    result = c.execute(query)
    ingredientes = result.fetchall()
    con.close()
    return ingredientes
def get_nombre():
    con = connect()
    c = con.cursor()
    query = """SELECT recetas.nombre FROM recetas,categorias where recetas.fk_id_categoria=categorias.id_categoria"""
    result = c.execute(query)
    nombre = result.fetchall()
    con.close()
    return nombre
def get_preparacion():
    con = connect()
    c = con.cursor()
    query = """SELECT recetas.preparacion FROM recetas, categorias where recetas.fk_id_categoria=categorias.id_categoria"""
    result = c.execute(query)
    preparacion = result.fetchall()
    con.close()
    return preparacion
def actualizar_receta(id_receta,nombre,fk_id_categoria,descripcion,preparacion,ingredientes,imagen,fk_id_pais):
    exito = False
    con = conectar()
    c = con.cursor()
    c.execute("UPDATE recetas SET nombre=?, ingredientes=?, preparacion=? WHERE id_receta=? AND fk_id_categoria=?",(id_receta,nombre,fk_id_categoria,descripcion,preparacion,ingredientes,imagen,fk_id_pais))
    con.commit()
    con.close()
    return True
def get_imagen():
	con=connect()
	c=con.cursor()
	query="""SELECT receta.imagen from recetas where recetas.fk_id_categoria=categorias.id_categoria"""
	result=c.execute(query)
	imagen=result.fetchall()
	con.close()
	return imagen
