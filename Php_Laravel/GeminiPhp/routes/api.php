<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Librote;
use Illuminate\Http\Request;
use Illuminate\Http\Response;

class LibroteController extends Controller
{
    public function index()
    {
        $libros = Librote::all();
        return response()->json($libros, Response::HTTP_OK);
    }

    public function store(Request $request)
    {
        $validatedData = $request->validate([
            'titulo' => 'required|string|max:255',
            'autor' => 'required|string',
            'anio_publicacion' => 'required|integer',
        ]);

        $librote = Librote::create($validatedData);

        return response()->json($librote, Response::HTTP_CREATED);
    }

    public function show(Librote $librote)
    {
        return response()->json($librote, Response::HTTP_OK);
    }

    public function update(Request $request, Librote $librote)
    {
        $validatedData = $request->validate([
            'titulo' => 'string|max:255',
            'autor' => 'string',
            'anio_publicacion' => 'integer',
        ]);

        $librote->update($validatedData);

        return response()->json($librote, Response::HTTP_OK);
    }

    public function destroy(Librote $librote)
    {
        $librote->delete();

        return response()->json(null, Response::HTTP_NO_CONTENT);
    }
}