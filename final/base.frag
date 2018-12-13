#version 150

// base fragment shader
//
// Contributor:  Hiteshi Shah

// INCOMING DATA

// Material properties of the teapot and quad
uniform vec4 base_ambient_material_color;
uniform float base_ambient_reflection_coefficient;
uniform vec4 base_diffuse_material_color;
uniform float base_diffuse_reflection_coefficient;
uniform vec4 base_specular_material_color;
uniform float base_specular_exponent;
uniform float base_specular_reflection_coefficient;

// Properties of the light source
uniform vec4 base_light_color;

// Properties of the ambient light
uniform vec4 base_ambient_light;

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
	vec4 ambient = base_ambient_material_color * base_ambient_reflection_coefficient * base_ambient_light;

	// diffuse
	vec4 diffuse = base_diffuse_material_color * base_diffuse_reflection_coefficient * (dot(L, N));

	// specular
	vec4 specular = base_specular_material_color * base_specular_reflection_coefficient * pow(max(0.0, dot(R, V)), base_specular_exponent);

	gl_FragColor = ambient + base_light_color * (diffuse + specular);
}
