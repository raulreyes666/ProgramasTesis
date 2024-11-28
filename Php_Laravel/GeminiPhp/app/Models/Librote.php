<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Librote extends Model
{
    use HasFactory;

    protected $fillable = [
        'titulo',
        'autor',
        'anio_publicacion',
    ];
}