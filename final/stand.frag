#version 150

// stand fragment shader
//
// Contributor:  Hiteshi Shah

// INCOMING DATA

// Material properties of the teapot and quad
uniform vec4 stand_ambient_material_color;
uniform float stand_ambient_reflection_coefficient;
uniform vec4 stand_diffuse_material_color;
uniform float stand_diffuse_reflection_coefficient;
uniform vec4 stand_specular_material_color;
uniform float stand_specular_exponent;
uniform float stand_specular_reflection_coefficient;

// Properties of the light source
uniform vec4 stand_light_color;

// Properties of the ambient light
uniform vec4 stand_ambient_light;

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
	vec4 ambient = stand_ambient_material_color * stand_ambient_reflection_coefficient * stand_ambient_light;

	// diffuse
	vec4 diffuse = stand_diffuse_material_color * stand_diffuse_reflection_coefficient * (dot(L, N));

	// specular
	vec4 specular = stand_specular_material_color * stand_specular_reflection_coefficient * pow(max(0.0, dot(R, V)), stand_specular_exponent);

	gl_FragColor = ambient + stand_light_color * (diffuse + specular);
}
