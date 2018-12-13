#version 150

// Texture mapping vertex shader
//
// Contributor:  Hiteshi Shah

// INCOMING DATA

uniform vec4 ambient_material_color;
uniform float ambient_reflection_coefficient;
uniform vec4 diffuse_material_color;
uniform float diffuse_reflection_coefficient;
uniform vec4 specular_material_color;
uniform float specular_exponent;
uniform float specular_reflection_coefficient;

// Properties of the light source
uniform vec4 light_color;

// Properties of the ambient light
uniform vec4 ambient_light;

in vec3 vNorm;
in vec3 light;
in vec3 vPos;

// Here is where you should add the variables you need in order
// to propogate data from the vertex shader to the fragment shader
// so that it can do the shading and texture mapping computations

in vec2 texCoord;

uniform sampler2D frontTexture;


void main()
{
    vec3 N = normalize(vNorm); // need for diffuse
    vec3 L = normalize(light - vPos);
    vec3 R = normalize (reflect(-L, N)); // need for specular
    vec3 V = normalize (-vPos);

    // ambient
    vec4 ambient = texture2D(frontTexture, texCoord) * ambient_reflection_coefficient * ambient_light;

    // diffuse
    vec4 diffuse = texture2D(frontTexture, texCoord) * diffuse_reflection_coefficient * (dot(L, N));

    // specular
    vec4 specular = texture2D(frontTexture, texCoord)  * specular_reflection_coefficient * pow(max(0.0, dot(R,V)), specular_exponent);

    gl_FragColor = (ambient + diffuse + specular);
}
