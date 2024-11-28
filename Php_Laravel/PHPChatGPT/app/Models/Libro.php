<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Libro extends Model
{
    use HasFactory;

    protected $fillable = [
        'titulo', 
        'anio_publicacion'
    ];

    // Si deseas personalizar el nombre de la tabla (en caso de que no sea 'libros'):
    // protected $table = 'nombre_de_tu_tabla';
}
