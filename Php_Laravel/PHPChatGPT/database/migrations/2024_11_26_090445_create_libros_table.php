<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateLibrosTable extends Migration
{
    public function up()
    {
        Schema::create('libros', function (Blueprint $table) {
            $table->id(); // ID autoincremental
            $table->string('titulo'); // Titulo del libro
            $table->year('anio_publicacion'); // Año de publicación
            $table->timestamps(); // Para los campos created_at y updated_at
        });
    }

    public function down()
    {
        Schema::dropIfExists('libros');
    }
}
