#version 150

// lamp fragment shader
//
// Contributor:  Hiteshi Shah

// INCOMING DATA

// Material properties of the teapot and quad
uniform vec4 lamp_ambient_material_color;
uniform float lamp_ambient_reflection_coefficient;
uniform vec4 lamp_diffuse_material_color;
uniform float lamp_diffuse_reflection_coefficient;
uniform vec4 lamp_specular_material_color;
uniform float lamp_specular_exponent;
uniform float lamp_specular_reflection_coefficient;

// Properties of the light source
uniform vec4 lamp_light_color;

// Properties of the ambient light
uniform vec4 lamp_ambient_light;

in vec3 vNorm;
in vec3 light;
in vec3 vPos;

void main()
{
	vec3 N = normalize(vNorm);
	vec3 L = normalize(light - vPos);
	vec3 R = normalize (reflect(-L, N));
    vec3 V = normalize (-vPos);

	// ambient
	vec4 ambient = lamp_ambient_material_color * lamp_ambient_reflection_coefficient * lamp_ambient_light;

	// diffuse
	vec4 diffuse = lamp_diffuse_material_color * lamp_diffuse_reflection_coefficient * (dot(L, N));

	// specular
	vec4 specular = lamp_specular_material_color * lamp_specular_reflection_coefficient * pow(max(0.0, dot(R, V)), lamp_specular_exponent);

	gl_FragColor = ambient + lamp_light_color * (diffuse + specular);
}
